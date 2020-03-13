











import sys
import os
def main():
    mk_base_configs_dir, coreip_mk, federation_root = sys.argv[1], sys.argv[2], sys.argv[3]
    flatten_py_tmp      = open(os.path.join(federation_root, "config.py.tmp"), "w+")
    mk_file_list_fp = [open(os.path.join(mk_base_configs_dir, coreip_mk), "r")]

    while mk_file_list_fp:
        content = mk_file_list_fp[-1].readline()
        if len(content)==0:
            mk_file_list_fp[-1].close()
            mk_file_list_fp.pop(-1)
        elif content.split(" ")[0] == "include" and content.split()[1].split("/")[0]=="$(mk_base_configs_dir)":
                file_name = content.split('/')[-1].strip("\n")
                mk_file_list_fp.append(open(os.path.join(mk_base_configs_dir, file_name), "r"))
        else:
            content = content.split("#")[0].rstrip("\t")
            flatten_py_tmp.write(content)
    flatten_py_tmp.close()

    flatten_py_tmp      = open(os.path.join(federation_root, "config.py.tmp"),  "r")
    flatten_py_tmp_2    = open(os.path.join(federation_root, "config.py.tmp2"), "w")

    while True:
        content = flatten_py_tmp.readline()
        if len(content) == 0:
            break
        elif content.split(" ")[0] == "mk_base_configs_dir":
            continue
        elif content.split(" ")[0] == "federation_root":
            continue
        elif len(content.split(" ")[-1].split("/")) >= 2:
            content_tmp     = content.strip("\n").split(" ")                # a = x/y/z --> [a, =, x/y/z]
            join_path       = content_tmp[-1].split("/")                    #x/y/z --> [x, y, z]
            join_path       = ["\"" + ele + "\"" for ele in join_path]      #[x, y, z] --> ["x", "y", "z"]
            content_tmp[-1] = "os.path.join(" + ",".join(join_path) + ")\n"
            content         = " ".join(content_tmp)
        else:
            sep = ""
            if "?="   in content      : sep = "?="
            elif ":=" in content      : sep = ":="
            elif "="  in content      : sep = "="
            if sep is not "":
                content_tmp     = content.split(sep)
                content_tmp[-1] = "\"" + content_tmp[-1].strip("\n").strip(" ") + "\"\n"
                content          = sep.join(content_tmp)
        content = content.replace("$(mk_base_configs_dir)",     mk_base_configs_dir)
        content = content.replace("$(federation_root)",         federation_root)
        flatten_py_tmp_2.write(content)

    flatten_py_tmp.close()
    flatten_py_tmp_2.close()


    os.system("cp " + os.path.join(federation_root, "config.py.tmp2") + " " + os.path.join(federation_root, "cfg.py"))


if __name__ == "__main__":
    main()