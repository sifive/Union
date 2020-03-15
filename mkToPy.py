

import os
import sys



keyword_list = [
        "define", "=", ":=", "?=", "endef", "ifdef", \
        "ifndef", "ifeq", "ifneq", "else", "endif", "include", \
        "-include", "subst", "patsubst", "strip", "findstring", \
        "filter", "dir", "notdir", "suffix", "basename", "addsuffix", \
        "addprefix", "join", "realpath", "abspath", "shell", \
        "origin", "foreach", "if", "then", "else", "for", "do", "in", \
        "done", "$@", "$<", "$?", "$(", "(", ")", ":", ".PHONY", "\\", \
        "{", "}", "\t", "echo", "@echo", "/"
]

keyword_dict = {
        "define"    : "DEF_START",
        "="         : "EXPAND_ASSIGNMENT",
        ":="        : "FIRST_ASSIGNMENT",
        "?="        : "EMPTY_ASSIGNMENT",
        "endef"     : "DEF_END",
        "ifdef"     : "IFDEF",
        "ifndef"    : "IFNDEF",
        "ifeq"      : "IFEQ",
        "ifneq"     : "IFNEQ",
        "else"      : "ELSE",
        "endif"     : "ENDIF",
        "include"   : "INCLUDE",
        "-include"  : "INCLUDE",
        "subst"     : "SUBST",
        "patsubst"  : "PATSUBST",
        "strip"     : "STRIP",
        "findstring": "FINDSTRING",
        "filter"    : "FILTER",
        "dir"       : "DIR",
        "notdir"    : "NOTDIR",
        "suffix"    : "SUFFIX",
        "basename"  : "BASENAME",
        "addsuffix" : "ADDSUFFIX",
        "addprefix" : "ADDPREFIX",
        "join"      : "JOIN",
        "realpath"  : "REALPATH",
        "abspath"   : "ABSPATH",
        "shell"     : "SHELL",
        "origin"    : "ORIGIN",
        "foreach"   : "FOREACH",
        "if"        : "IF",
        "then"      : "THEN",
        "else"      : "ELSE",
        "for"       : "FOR",
        "do"        : "DO",
        "in"        : "IN",
        "done"      : "DONE",
        "$@"        : "TARGET_NAME",
        #"$%"       : "KEYWORD",
        "$<"        : "FIRST_DEP",
        "$?"        : "ALL_DEP",
        #"$^"       : "KEYWORD",
        #"$+"       : "KEYWORD",
        "$("        : "VARIABLE_LEFT_PAR",
        "("         : "LEFT_PAR",
        ")"         : "RIGHT_PAR",
        ":"         : "SEP",
        ".PHONY"    : "PHONY",
        "\\"        : "BACKSLASH",
        "{"         : "LEFT_BRACKET",
        "}"         : "RIGHT_BRACKET",
        "\t"        : "TAB",
        "echo"      : "ECHO",
        "@echo"     : "ECHO",
        "/"         : "SLASH",
}



rule_tuple_list = [
        ("PROG_START"            , ["PROGRAM"]),
        ("PROGRAM"               , ["PROGRAM", "STATEMENT"]),
        ("PROGRAM"               , ["STATEMENT"]),
        ("PROGRAM"               , ["PROGRAM", "DEF_START", "EXPAND_ASSIGNMENT", "VARIABLE"]),
        ("PROGRAM"               , ["PROGRAM", "DEF_START", "FIRST_ASSIGNMENT",  "VARIABLE"]),
        ("PROGRAM"               , ["PROGRAM", "DEF_START", "EMPTY_ASSIGNMENT",  "VARIABLE"]),
        ("PROGRAM"               , ["PROGRAM", "DEF_START", "MULTI_LINE", "DEF_END"]),
        ("PROGRAM"               , ["PROGRAM", "TARGET_LIST", "SEP"]),
        ("PROGRAM"               , ["PROGRAM", "TARGET_LIST", "SEP", "PRE_REQUISITES_LIST", "ACTION"]),
        ("TARGET_LIST"           , ["TARGET_LIST", "TARGET"]),
        ("TARGET"                , ["VARIABLE"]),
        ("TARGET"                , []),
        ("PRE_REQUISITEST_LIST"  , ["PRE_REQUISITES_LIST", "PRE_REQUISITE"]),
        ("MULTI_LINE"            , ["MULTI_LINE", "STATEMENT"]),
        ("MULTI_LINE"            , ["STATEMNT"]),
        ("STATEMENT"             , ["INCLUDE", "FILE"]),
        ("STATEMENT"             , ["STRING", "COLON", "VARIABLE"]),
        ("STATEMENT"             , []),
        ("STATEMENT"             , ["IF_STATEMENT", "THEN_STATEMENT"]),
        ("STATEMENT"             , ["IF_STATEMENT", "THEN_STATEMENT", "ELSE_STATEMENT"]),
        ("IF_STATEMENT"          , ["IF", "CONDITION"]),
        ("THEN_STATEMENT"        , ["THEN", "STATEMENTS"]),
        ("ELSE_STATEMENT"        , ["ELSE", "STATEMENTS"]),
        ("FOR_STATEMENT"         , ["FOR", "VARIABLE", "IN", "VARAIBLE", "SEMICOLON", "DO", "ACTION", "DONE"]),
        ("ACTION"                , ["ECHO", "STRING"]),
        ("ACTION"                , ["FOR_STATEMENT"]),
]


class content_type():
    def __init__(self, content, keyword):
        self.content = content
        self.keyword = keyword

    def __str__(self):
        return self.keyword + " " + self.content

class matcher():
    def __init__(self):
        self.isStringStart  = False
        self.isStringEnd    = False
        self.consumeCnt     = 0
        self.buffer         = ""
        self.shouldEval     = False
        self.forFollowedByE = False

    def consume(self, string):
        if self.consumeCnt >= len(string)-1:
            return True
        if string[self.consumeCnt] is not "\"" and \
                string[self.consumeCnt] is not " " and \
                string[self.consumeCnt] is not "\'" and \
                string[self.consumeCnt] is not "\n" and \
                string[self.consumeCnt] is not "\t":
            self.buffer += string[self.consumeCnt]
        self.consumeCnt = self.consumeCnt + 1

        if string[self.consumeCnt]   == "\"" and self.isStringStart is False:
            self.isStringStart  = True
            self.isStringEnd    = False
        elif string[self.consumeCnt] == "\"" and self.isStringStart is True:
            self.isStringEnd    = True
        elif string[self.consumeCnt] == " ":
            self.shouldEval     = True
        elif string[self.consumeCnt] == "\t":
            self.shouldEval     = True
        elif string[self.consumeCnt] == "\n":
            self.shouldEval     = True
        elif string[self.consumeCnt] == ")":
            self.shouldEval     = True
        if self.buffer == "for" and string[self.consumeCnt] == 'e':
            self.forFollowedByE = True
        else:
            self.forFollowedByE = False
        return False


    def eval(self):
        if self.isStringEnd is True:
            self.isStringStart  = False
            self.isStringEnd    = False
            rtn_val             = self.buffer
            self.buffer         = ""
            return "STRING", rtn_val

        elif self.shouldEval is True and self.forFollowedByE is False:
            self.shouldEval     = False
            if self.buffer in keyword_list:
                rtn_val     = self.buffer
                self.buffer = ""
                return keyword_dict[rtn_val], rtn_val

            else:
                rtn_val     = self.buffer
                if self.buffer.endswith(")"):
                    self.buffer = ")"
                else:
                    self.buffer = ""
                return "VARIABLE", rtn_val.rstrip(")")

        elif self.buffer in keyword_list and self.forFollowedByE is False:
                rtn_val     = self.buffer
                self.buffer = ""
                return keyword_dict[rtn_val], rtn_val

        else:
            return None, ""

def stripComment(file_content):
    rtn_content = [fc for fc in file_content if not fc.strip("\t").startswith("#")]
    return rtn_content



def tokenize(file_content):
    tokens = []
    for fc in file_content:
        tmp = matcher()
        while True:
            isEnd = tmp.consume(fc)
            if isEnd:
                break
            Type, val = tmp.eval()
            if Type is not None:
                tokens.append(content_type(val, Type))

    return tokens


#def syntax_analyze(tokens):




def main():
    in_file_name    = sys.argv[1]
    input_file      = open(os.path.join(".", in_file_name), "r")
    file_content    = input_file.readlines()
    file_content_nc = stripComment(file_content)
    tokens          = tokenize(file_content_nc)
    #syntax_tree     = syntax_analyze(tokens)
    #output_python(syntax_tree)
    for t in tokens:
        print(t)



if __name__ == "__main__":
    main()