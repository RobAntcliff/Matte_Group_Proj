import lxml
import re # regexy 
import sys
import itertools
from drugdict import *  

lextokens = iter([])

LEXTOKENS = ( (r'process[ \n\t{]'         , "PROCESS") 
            , (r'sequence[ \n\t{]'        , "SEQUENCE")
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

def parse(data):
    global lextokens
    lextokens =lexer(data, LEXTOKENS)
    par =parseProc()
    return par

def lexer(data, exprs):
    head =0
    while head < len(data):
        for (syms, t) in exprs:
            regex = re.compile(syms,flags = re.DOTALL|re.MULTILINE)
            check = regex.match(data, head)
            if check:
                dat =check.group(0)
                if t:
                    yield (dat, t)
                head=check.end(0)
                break
        else:
            raise ReturnExcept('Error char -> "%s"\n' % data[head]) #nomatch

def addToken(value):
    global lextokens
    lextokens = itertools.chain([value], lextokens)

def nextTok():
    try:
        next_tok = next(lextokens)
    except StopIteration:
        raise ReturnExcept('file end error') 
    return next_tok

def lookahead(tag):
    (dat, t) =nextTok()
    if tag == t:
        return dat
    else:
        addToken((dat, t))
        return False

def lookahead_f(tag):
    (dat, t) = nextTok()
    if tag != t:
        raise ReturnExcept('Expect %s, not "%s"\n' % (tag,dat))
    return dat

def error_with_message(curr_location):
    (dat, t) = nextTok()
    raise ReturnExcept('Unexpected %s ("%s") parsed %s'%(t, dat, curr_location))

def parseProc():
    lookahead_f("PROCESS")
    idt = lookahead_f("ID")
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
    else:
        error_with_message("err prims")

def flow(cnFlow):
    c = { "flow": cnFlow }
    ident = lookahead("ID")
    if ident:
        c["name"] = ident
    c["actions"] = utilFuncLi(prim)
    return c

def action():
    idt = lookahead_f("ID")
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
    lookahead_f("LEFTBRACKET")
    if basType in ["provides", "requires", "agent"]:
        p = parseEx()
    else:
        p = lookahead_f("STRING")
    lookahead_f("RIGHTBRACKET")
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
        return {"attr": attrCheck}
    idt = lookahead("ID")
    if idt:
        t = {"attr":idt}
        if lookahead("POINT"):
            t['n_id'] = lookahead_f("ID")
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
    lookahead_f("LEFTBRACKET")
    while not lookahead("RIGHTBRACKET"):
        items.append(par())
    return items

class ReturnExcept(Exception):pass

def main():
    f = open(sys.argv[1],"r")
    contents = f.read()
    parsed = parse(contents)
    print parsed

if __name__ == "__main__":
    main()