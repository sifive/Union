






import os
import sys


ASSIGNMENT = [":=", "?=", "+=", "="]
RESERVE_WORD = [
        "define",\
        "endef",\
        "undefine",\
        "ifeq",\
        "ifneq",\
        "else",\
        "endif",\
        "include",\
        "-include",\
        "override",\
        "export",\
        "unexport",\
        "private",\
        "vpath"
]

RESERVE_CMD = [
        "subst",\
        "patsubst",\
        "strip",\
        "findstring",\
        "filter",\
        "filter-out",\
        "sort",\
        "word",\
        "words",\
        "wordlist",\
        "firstword",\
        "lastword",\
        "dir",\
        "notdir",\
        "suffix",\
        "basename",\
        "addsuffix",\
        "addprefix",\
        "join",\
        "wildcard",\
        "realpath",\
        "abspath",\
        "error",\
        "warning",\
        "shell",\
        "origin",\
        "flavor",\
        "foreach",\
        "eval",\
        ]


def strip_comment(content):
    return [c for c in content if not c.startswith("#")]


def resolve_name(value, variable_table):
    while(value.find("$(") is not -1):
        variable_to_replace = value[value.find("$(")+2 : value.find(")")]
        if variable_to_replace not in variable_table:
            break
        value = value.replace("$(" + variable_to_replace + ")", variable_table[variable_to_replace])
    return value


def isComment(content):
    return content.startswith("#")

def readAllMakefile(makefile):
    rtn_content_list    = []
    mk_common_dir       = os.path.dirname(os.path.abspath(makefile))
    mk_base_configs_dir = os.path.abspath(os.path.join(mk_common_dir, "..", "base_configs"))
    mk_common_dir       = os.path.abspath(os.path.join(mk_common_dir, "..", "common"))
    federation_root     = os.path.abspath(os.path.join(mk_common_dir, "..", ".."))
    base_mk             = os.path.join(federation_root, "mk", "common", "base.mk")
    toBeRead            = [open(base_mk, "r"), open(makefile, "r")]
    variable_tmp_table  = {
        "mk_common_dir"         : mk_common_dir,
        "mk_base_configs_dir"   : mk_base_configs_dir,
        "federation_root"       : federation_root
    }

    while toBeRead:
        var_name, value = "", "" #just to make it global
        append_next_line = False
        if append_next_line:
            tmp_content += toBeRead[-1].readline()
        else:
            tmp_content = toBeRead[-1].readline()

        if isComment(tmp_content):
            continue

        if len(tmp_content) == 0:
            toBeRead[-1].close()
            toBeRead.pop()
            continue

        if tmp_content.startswith("include "):
            open_file = resolve_name(tmp_content.strip("\n").split(" ")[1], variable_tmp_table)
            #print(open_file)
            toBeRead.append(open(open_file))
            continue

        else:
            sep = ""
            for assignment in ASSIGNMENT:
                if assignment in tmp_content:
                    sep = assignment
                    break
            if sep == "":
                rtn_content_list.append(tmp_content)
            else:
                if append_next_line is False:
                    var_name, value = tmp_content.split(sep)[0].strip(" "), tmp_content.split(sep)[1].strip(" \n")
                if "mk_common_dir" in var_name or "mk_base_configs_dir" in var_name or "federation_root" in var_name:
                    continue
                if value.endswith("\\"):
                    tmp_content = value.strip("\\")
                    append_next_line = True
                else:
                    append_next_line = False
                    if sep == "?=" and (var_name not in variable_tmp_table or variable_tmp_table[var_name]==""):
                        variable_tmp_table[var_name] = resolve_name(value, variable_tmp_table)
                    if sep == ":=" and var_name not in variable_tmp_table:
                        variable_tmp_table[var_name] = resolve_name(value, variable_tmp_table)
                    if sep == "+=":
                        if var_name not in variable_tmp_table:
                            variable_tmp_table[var_name] = resolve_name(value, variable_tmp_table)
                        else:
                            variable_tmp_table[var_name] += (" " + resolve_name(value, variable_tmp_table))
                    if sep == "=" :
                        variable_tmp_table[var_name] = resolve_name(value, variable_tmp_table)

    return rtn_content_list, variable_tmp_table


def print_table(dictionary):
    print("\n=============================variable_table_start===================================")
    for d in dictionary:
        print(d + ": " + dictionary[d])
    print("=============================variable_table_ends===================================\n")


def build_define_assignment_table(content):
    rtn_assignment_table = []
    rtn_define_table = []
    def_start = False
    define_table_content = ""
    for c in content:
    #normal assignment
        #if    " ="  in c:
        #    rtn_assignment_table.append((c.strip("\n").split("="),  "EXPAND_ASSIGNMENT"))
        #elif  " ?=" in c:
        #    rtn_assignment_table.append((c.strip("\n").split("?="), "EMPTY_ASSIGNMENT"))
        #elif  " :=" in c:
        #    rtn_assignment_table.append((c.strip("\n").split(":="), "FIRST_ASSIGNMENT"))
        #elif  " +=" in c:
        #    rtn_assignment_table.append((c.strip("\n").split("+="), "APPEND_LIST"))
    #multiline definition
        if "define" in c and def_start is False:
            def_start = True
            variable_name = c.strip("\n").split(" ")[1]
            continue
        if def_start is True and "endef" == c.strip("\n"):
            def_start = False
            rtn_define_table.append((variable_name, define_table_content))
            define_table_content = ""
            continue
        if def_start is True:
            define_table_content += c
    #other
        #Don't mind condition
    return rtn_assignment_table, rtn_define_table

def main():
    makefile                    = sys.argv[1]
    content, variable_table     = readAllMakefile(makefile)
    #strip_content               = strip_comment(content)
    #_, define_table             = build_define_assignment_table(strip_content)

    for vt in variable_table:
        print(vt + ": " + variable_table[vt])

    #for vt in variable_table:
    #    print(vt)
    #    print("\n")
    #for dt in define_table:
    #    print(dt)
    #    print("\n")



if __name__ == "__main__":
    main()