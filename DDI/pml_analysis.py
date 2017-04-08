import lxml
import re # regexy 
import sys
import itertools
from DDI.drugdict import drugDict
from DDI.timedict import timeDict
from DDI.freqdict import freqDict
from DDI.parser_utils import *

LEXTOKENS = ( (r'process[ \n\t{]'         , "PROCESS") 
            , (r'sequence[ \n\t{]'        , "SEQUENCE")
            , (r'task[ \n\t{]'            , "TASK")
            , (r'selection?[ \n\t{]'      , "SELECTION")
            , (r'script[ \n\t{]'          , "SCRIPT")
            , (r'branch[ \n\t{]'          , "BRANCH")
            , (r'agent'                   , "AGENT")
            , (r'iteration[ \n\t{]'       , "ITERATION")
            , (r'action[ \n\t{]'          , "ACTION")
            , (r'manual'                  , "MANUAL")
            , (r'executable'              , "EXECUTABLE")
            , (r'requires'                , "REQUIRES")
            , (r'provides'                , "PROVIDES")
            , (r'tool'                    , "TOOL")
            , (r'time'                    , "TIME")
            , (r'frequency'               , "FREQUENCY")
            , (r'delay'                   , "DELAY")
            , (r'[_A-Za-z][_A-Za-z0-9]*'  , "ID")
            , (r'\.'                      , "POINT")
            , (r'[0-9]+'                  , "NUM")
            , (r'"[^"]*"'                 , "STRING")
            , (r'(>=?)|(<=?)|(==)|(!=)'   , "COMPARE")
            , (r'(\|\|)|(&&)'             , "CONJUCT")
            , (r'{'                       , "LEFTBRACKET")
            , (r'}'                       , "RIGHTBRACKET")
            , (r'/\*((?!(\*/)).)*\*/'     , None)
            , (r'[ \n\t]+'                , None)
            )

sys.tracebacklimit = None

def findConsClash():
    checkForClashes(clashes)
    if not clashFinal:
        print("No Construct name clashes in PML file.")
    else:
        for cname in clashes:
            printClashes(cname)

def checkForClashes(clashes):
    for i in clashes:
        for j in consRef:
            if j[2] == i and str(i) != 'False':
                clashFinal.append(j)

def printClashes(cname):
    print("Construct name clash occured : Name -> " + str(cname))
    for i in clashFinal:
        ctype = i[0]
        ln = i[3]
        print("Construct Type -> " + ctype + " : Line number -> " + str(ln) +".")

def findTaskUsed():
    return taskCheck

def run(f):
    resetVars()
    contents = f.read()
    parsed = parse(contents)
    drugsLi = findDrugs(tempList)
    return errList

def parse(data):
    global lextokens
    lextokens =lexer(data, LEXTOKENS)
    par =parseProc()
    return par

def getDrugs():
    return findDrugs(tempList)

def getDel():
    x = findDelays()
    if not x: 
        return [] 
    else: 
        return x

def getDelays():
    delays = []
    i = 0
    while i < len(tempList):
        if "minutes" in tempList[i]:
            if tempList[i] != "0 minutes":
                delays.append("Action: " + tempList[i -4] + ", Specifically: " + tempList[i-3] + ", Delay: " + tempList[i])
        i = i + 1
    return delays

def getDrugsTimeAndFrequency():
    x = findDrugsTimeAndFrequency()
    if not x:
        return []
    else:
        return x

def findDrugs(list):
    drugList = []
    for i in list: 
        if i in drugDict.keys() and i not in drugList:
            drugList.append(i)
    return drugList

def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)

def findDrugsTimeAndFrequency():
    key = 0
    for i in outDrugsTimeDict:
        act = outDrugsTimeDict.get(i)
        test = checkDrugs(act)
        if test and len(act) == 1:
            dtfDict[key] = act
            key += 1
        elif test and len(act) > 1:
            if len(act) == 2:
                act = sortActOne(act)
                dtfDict[key] = act
                key += 1
            elif len(act) == 3: 
                act = sortActTwo(act)
                dtfDict[key] = act
                key += 1
    return dtfDict

def findDelays():
    for key, val in outDelayDict.items():
        if len(val) > 0:
            delDict[key] = val
    return delDict

def checkDrugs(list):
    hasDrug = False
    for i in list:
        if i in drugDict.keys():
            hasDrug = True 
    return hasDrug

def sortActOne(list):
    for i, item in enumerate(list):
        if item in drugDict:
            if list[0] != item:
                list = swap(list, i, 0, item)
    return list

def sortActTwo(list):
    for i, item in enumerate(list):
        if item in drugDict:
            if list[0] != item:
                list = swap(list, i, 0, item)
        elif item in timeDict:
            if list[1] != item:
                list = swap(list, i, 1, item)
        elif item in freqDict: 
            if list[2] != item:
                list = swap(list, i, 2, item)
    return list

def clear(list):
    for i in list:
        list[:] = [x for x in list if x in drugDict or x in timeDict or x in freqDict]
    return list 

def swap(li, i, n, itm):
    tmp = li[n] 
    li[n] = itm
    li[i] = tmp
    return li

def lexer(data, exprs):
    head =0
    while head < len(data):
        for (syms, t) in exprs:
            regex = re.compile(syms)
            check = regex.match(data, head)
            if check:
                dat =check.group(0)
                if t:
                    yield (dat, t)
                head=check.end(0)
                break
        else:
            raise ErrorReport('Error char -> "%s"\n' % data[head]) 

def addToken(value):
    global lextokens
    lextokens = itertools.chain([value], lextokens)

def nextTok():
    try:
        next_tok = next(lextokens)
    except StopIteration:
        raise ErrorReport('file end error') 
    return next_tok

def lookahead(tag):
    (dat, t) =nextTok()
    if tag == t:
        return dat
    else:
        addToken((dat, t))
        return False

def lookahead_f(tag, const_name):
    (dat, t) = nextTok()
    if tag != t:
        err_str = "Type -> " + str(const_name) + " : Line Number -> " +  str(lineNum) + " : Expecting -> " + str(tag) + ", Received -> " + str(dat)
        errList.append(err_str)
    return dat
    
def error_with_message(curr_location):
    (dat, t) = nextTok()
    err_str = "Unexpected " + str(t) + "(" + str(dat) + ") parsed " + str(curr_location)
    errList.append(err_str)
    print('Unexpected %s ("%s") parsed %s'%(t, dat, curr_location))

def parseProc():
    lookahead_f("PROCESS", "Process")
    idt = lookahead_f("ID","Process")
    checkClashes(consNames, idt)
    consNames.append(idt)
    tup = ("Process", procCnt, idt, lineNum)
    consRef.append(tup)
    incProcCnt()
    ps = utilFuncLi(getPrimitive)
    r = { "actions": ps, "process name": idt }
    return r

def getPrimitive():
    if lookahead("ACTION"):
        return action()
    elif lookahead("SEQUENCE"):
        return flow("sequence")
    elif lookahead("SELECTION"):
        return flow("selection")
    elif lookahead("ITERATION"):
        return flow("iteration")
    elif lookahead("BRANCH"):
        return flow("branch")
    elif lookahead("TASK"):
        return flow("task")
    else:
        (dat, t) = nextTok()

def flow(construct):
    if construct == "task":
        x = ("task", lineNum)
        taskCheck.append(x)
    c = { "construct type": construct }

    ident = lookahead("ID")
    checkClashes(consNames, ident)
    consNames.append(ident)
    consCnt = incConsCnt(construct)
    tup = (construct, consCnt, ident, lineNum)
    consRef.append(tup)

    if ident:
        c["construct name"] = ident
    c["actions"] = utilFuncLi(getPrimitive)
    return c

def action():
    idt = lookahead_f("ID", "Action")
    actNm = idt

    if lookahead("MANUAL"):
        t = "manual"
    elif lookahead("EXECUTABLE"):
        t = "executable"
    else:
        t = "not specified"

    checkClashes(consNames, idt)
    consNames.append(idt)
    tup = ("action", actCnt, idt, lineNum)
    consRef.append(tup)
    incActCnt()
    a = { "action name": idt, "construct type": "action", "action type" : t}
    for (ty, dat) in utilFuncLi(parseType):
        a[ty] = dat
    return a

def checkClashes(nmLi, name):
    if name in consNames and name not in clashes:
        clashes.append(name)

def parseType():
    basType = None
    if lookahead("AGENT"):
        basType = "agent"
    elif lookahead("SCRIPT"):
        basType = "script"
    elif lookahead("TOOL"):
        basType = "tool"
    elif lookahead("PROVIDES"):
        basType = "provides"
    elif lookahead("REQUIRES"):
        basType = "requires"
    elif lookahead("TIME"):
        basType = "time"
    elif lookahead("FREQUENCY"):
        basType = "frequency"
    elif lookahead("DELAY"):
        basType = "delay"

    x = lookahead_f("LEFTBRACKET", "Left Bracket")
    incLineNum()
    if basType in ["requires", "time", "frequency", "delay"]:
        p = parseEx(basType)
    else:
        p = lookahead_f("STRING", "String")
    lookahead_f("RIGHTBRACKET", "Right Bracket")
    r = (basType, p)
    return r

def compExpr(typ):
    r = {"left": constDesc(typ)}
    rel = lookahead("COMPARE")
    if rel:
        r['rel'] = rel
        r['right'] = constDesc(typ)
    return r

def constDesc(typ):
    dc = lookahead("NUM") or lookahead("STRING")
    if dc:
        dc = dc[1:-1]
        outDrugsTimeDict.setdefault(actCnt, [])
        outDelayDict.setdefault(actCnt, [])
        if dc in drugDict or dc in timeDict or dc in freqDict:
            outDrugsTimeDict[actCnt].append(dc)
        elif typ == "delay": 
            outDelayDict[actCnt].append(dc)
        tempList.append(dc)
        return {"description": dc}
    idt = lookahead("ID")
    if idt:
        t = {"description":idt}
        if lookahead("POINT"):
            t['n_id'] = lookahead_f("ID","val expr")
        return t

def parseEx(typ):
    a =[compExpr(typ)]
    ch_op = lookahead("CONJUCT")
    while(ch_op):
        comp = compExpr(typ)
        comp['conjunct'] = ch_op
        a.append(comp)
        ch_op = lookahead("CONJUCT")
    return a

def utilFuncLi(par):
    items = []
    check = lookahead_f("LEFTBRACKET", "Left Bracket")
    incLineNum()
    while not lookahead("RIGHTBRACKET"):
        items.append(par())
    incLineNum()
    return items

def containsDrugs(list):
    if not list:
        return False
    else:
        return True

def output(list):
    if containsDrugs(list):
        print(list)
        del tempList[:]
    else:
        print('No drugs in PML file')

def resetVars():
    del consNames[:]
    del consRef[:]
    del taskCheck[:]
    del clashes[:]
    del clashFinal[:]
    del errList[:]
    del tempList[:]
    dtfDict.clear()
    outDrugsTimeDict.clear()
    outDelayDict.clear()
    delDict.clear()
    resetLN()
    resetTskCnt()
    resetSelCnt()
    resetBchCnt()
    resetItrCnt()
    resetActCnt()

def incConsCnt(consType):
    if consType == "sequence":
        x = seqCnt
        incSeqCnt()
    elif consType == "task":
        x = taskCnt
        incTaskCnt() 
    elif consType == "selection":
        x = selCnt 
        incSelCnt()
    elif consType == "branch":
        x = branchCnt 
        incBranchCnt()
    elif consType == "iteration":
        x = iterCnt 
        incIterCnt()
    return x

def incActCnt():
    global actCnt
    actCnt += 1

def incProcCnt():
    global procCnt
    procCnt += 1

def incSeqCnt():
    global seqCnt
    seqCnt += 1

def incSelCnt():
    global selCnt
    selCnt += 1

def incTaskCnt():
    global taskCnt
    taskCnt += 1

def incBranchCnt():
    global branchCnt
    branchCnt += 1

def incIterCnt():
    global iterCnt 
    iterCnt += 1

def incLineNum():
    global lineNum
    lineNum += 1

def incLineNum():
    global lineNum
    lineNum += 1

def resetLN():
    global lineNum
    lineNum=1

def resetTskCnt():
    global taskCnt
    taskCnt = 1

def resetSelCnt():
    global selCnt
    selCnt = 1

def resetBchCnt():
    global branchCnt
    branchCnt = 1

def resetItrCnt():
    global iterCnt
    iterCnt = 1

def resetActCnt():
    global actCnt
    actCnt = 0

class ErrorReport(Exception):pass




