import lxml
import re # regexy 
import sys
import itertools
from DDI.drugdict import drugDict
from DDI.parser_utils import *

parsed = ""

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
        resetVars()
    else:
        for cname in clashes:
             printClashes(cname)
             resetVars()

def checkForClashes(clashes):
    for i in clashes:
        for j in consRef:
            if j[2] == i:
                clashFinal.append(j)

def printClashes(cname):
    print("Construct name clash occured : Name -> " + cname)
    for i in clashFinal:
        ctype = i[0]
        ln = i[3]
        print("Construct Type -> " + ctype + " : Line number -> " + str(ln) +".")

def getConsDeets(f):
    ct = f.read()
    parsed = parse(ct)
    print(consRef)
    resetLN()
    resetVars()

def findTaskUsed():
    if not taskCheck:
        print("Task construct not used in PML file.")
    else:
        print("Task construct is now deprecated, please use Sequence in its place.")
        if len(taskCheck) > 1:
            print("Task was used at lines ")
            for i in taskCheck:
                print([i][1]) 
                print(" ")
        else:
            print("Task was used at line " + str(taskCheck[0][1]) + ".")
    resetVars()

def run(f):
    contents = f.read()
    parsed = parse(contents)
    drugsLi = findDrugs(tempList)
    resetVars()
    output(drugsLi)

def findUnnamedC():
    resetVars()
    return parsed

def parse(data):
    global lextokens
    lextokens =lexer(data, LEXTOKENS)
    par =parseProc()
    return par

def findDrugs(list):
    drugList = []
    for i in list: 
        if i in drugDict.keys() and i not in drugList:
            drugList.append(i)
    return drugList

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
        raise ErrorReport('Unnamed Construct found : Construct type -> "%s" : Line Number -> "%s" : Expecting -> "%s" Name, Received -> "%s".\n' % (const_name,lineNum,tag,dat))
    return dat

def error_with_message(curr_location):
    (dat, t) = nextTok()
    raise ErrorReport('Unexpected %s ("%s") parsed %s'%(t, dat, curr_location))

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
        error_with_message("construct error")

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
    else:
        error_with_message("basic type error")
    x = lookahead_f("LEFTBRACKET", "lb")
    incLineNum()
    if basType in ["provides", "requires", "agent"]:
        p = parseEx()
    else:
        p = lookahead_f("STRING", "str")
    lookahead_f("RIGHTBRACKET", "rb")
    r = (basType, p)
    return r

def compExpr():
    r = {"left": constDesc()}
    rel = lookahead("COMPARE")
    if rel:
        r['rel'] = rel
        r['right'] = constDesc()
    return r

def constDesc():
    descripCheck = lookahead("NUM") or lookahead("STRING")
    if descripCheck:
        descripCheck = descripCheck[1:-1]
        tempList.append(descripCheck)
        return {"description": descripCheck}
    idt = lookahead("ID")
    if idt:
        t = {"description":idt}
        if lookahead("POINT"):
            t['n_id'] = lookahead_f("ID","val expr")
        return t
    error_with_message("description")

def parseEx():
    a =[compExpr()]
    ch_op = lookahead("CONJUCT")
    while(ch_op):
        comp = compExpr()
        comp['conjunct'] = ch_op
        a.append(comp)
        ch_op = lookahead("CONJUCT")
    return a

def utilFuncLi(par):
    items = []
    check = lookahead_f("LEFTBRACKET", "lb")
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
    del descrLi[:]
    del consRef[:]
    del taskCheck[:]
    del clashes[:]
    del clashFinal[:]
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
    actCnt = 1

class ErrorReport(Exception):pass




