import lxml
import re # regexy 
import sys
import itertools
from pmlfiles.drugdict import drugDict

#python pml_analysis.py pmlfiles/drugs.pml           -> returns list of drugs
#python pml_analysis.py pmlfiles/nodrugs.pml         -> outputs 'No drugs in PML file' to terminal 
#python pml_analysis.py pmlfiles/error.pml_analysis  -> finds error and returns it

lextokens = iter([])

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

tempList = []
sys.tracebacklimit = None

def parse(data):
    global lextokens
    lextokens =lexer(data, LEXTOKENS)
    par =parseProc()
    return par

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

def findDrugs(list):
    drugList = []
    for i in list: 
        if i in drugDict.keys() and i not in drugList:
            drugList.append(i)
    return drugList

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
        print('Expecting %s %s Name, but received "%s"\n' % (const_name,tag,dat))
        return -1
    return dat

def error_with_message(curr_location):
    (dat, t) = nextTok()
    raise ErrorReport('Unexpected %s ("%s") parsed %s'%(t, dat, curr_location))

def parseProc():
    check = lookahead_f("PROCESS", "Process")
    if check == -1:
        return -1
    idt = lookahead_f("ID","Process")
    if idt == -1:
        return -1
    ps = utilFuncLi(getPrimitive)
    r = { "actions": ps, "name": idt }
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

def flow(cnFlow):
    c = { "flow": cnFlow }
    ident = lookahead("ID")
    if ident:
        c["name"] = ident
    c["actions"] = utilFuncLi(getPrimitive)
    return c

def action():
    idt = lookahead_f("ID", "Action")
    if lookahead("MANUAL"):
        t = "manual"
    elif lookahead("EXECUTABLE"):
        t = "executable"
    else:
        t = ""
    a = { "name": idt, "cflow": "action", "type" : t}
    for (ty, dat) in utilFuncLi(parseType):
        a[ty] = dat
    return a

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
    else:
        error_with_message("basic type error")
    lookahead_f("LEFTBRACKET", "lb")
    if basType in ["provides", "requires", "agent"]:
        p = parseEx()
    else:
        p = lookahead_f("STRING", "str")
    lookahead_f("RIGHTBRACKET", "rb")
    r = (basType, p)
    return r

def compExpr():
    r = {"left": valueEx()}
    rel = lookahead("COMPARE")
    if rel:
        r['rel'] = rel
        r['right'] = valueEx()
    return r

def valueEx():
    attrCheck = lookahead("NUM") or lookahead("STRING")
    if attrCheck:
        attrCheck = attrCheck[1:-1]
        tempList.append(attrCheck)
        return {"attr": attrCheck}
    idt = lookahead("ID")
    if idt:
        t = {"attr":idt}
        if lookahead("POINT"):
            t['n_id'] = lookahead_f("ID","val expr")
        return t
    error_with_message("Expr")

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
    lookahead_f("LEFTBRACKET", "lb")
    while not lookahead("RIGHTBRACKET"):
        items.append(par())
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

class ErrorReport(Exception):pass

def run(f):
    contents = f.read()
    parsed = parse(contents)
    drugsLi = findDrugs(tempList)
    output(drugsLi)

def runParser(f):
    ct = f.read()
    parsed = parse(ct)
    #print(parsed)
    print("No errors found")
