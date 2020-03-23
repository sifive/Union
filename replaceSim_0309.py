





import os
import sys
import subprocess

federation_root         = ""
wake_build              = ""
file_index_json         = ""
rocketchip_root         = ""
firrtl_tool_src_root    = ""
firrtl_jar              = ""
federation_jar          = ""
firrtl_build_dir        = ""
verilog_build_conf      = ""
memgen_build_dir        = ""


FIRRTL_TRANSFORMS    = [\
	"sifive.enterprise.firrtl.MemToRegOfVecTransform" \
	,"firrtl.passes.InlineInstances" \
	,"sifive.enterprise.firrtl.ExampleTransform" \
	,"sifive.enterprise.firrtl.DontDedupTestHarnessSeqMems" \
	,"sifive.enterprise.firrtl.InjectDUTHierarchyTransform" \
	,"sifive.enterprise.firrtl.ExtractSeqMems" \
	,"sifive.enterprise.firrtl.ExtractSAGETransform" \
	,"sifive.enterprise.firrtl.ExtractClockGates" \
	,"sifive.enterprise.firrtl.ExtractBlackBoxesTransform" \
	,"sifive.enterprise.firrtl.SitestBlackBoxesTransform" \
	,"sifive.enterprise.firrtl.AddSeqMemPortsTransform" \
	,"sifive.enterprise.firrtl.ObfuscationTransform" \
	,"sifive.enterprise.firrtl.CoverPropReportTransform" \
	,"sifive.enterprise.firrtl.PrefixModulesTransform" \
	,"sifive.enterprise.firrtl.AddPreset" \
	,"sifive.enterprise.firrtl.TestHarnessHierarchyTransform" \
	,"sifive.enterprise.firrtl.SeqMemPathTransform" \
	,"sifive.enterprise.firrtl.HoistPassThroughConnections" \
	,"sifive.enterprise.grandcentral.GrandCentralTransform" \
	,"sifive.enterprise.firrtl.ExtractTestCodeTransform" \
	,"sifive.enterprise.firrtl.ModuleHierarchyTransform" \
	,"sifive.enterprise.firrtl.FileListTransform" \
	,"sifive.enterprise.firrtl.RegMappingTransform" \
	,"sifive.enterprise.firrtl.RetimeModulesTransform"
	]


def formattedStr(first, second):
    return "\"" + first + "\": " + "\"" + second + "\",\n"


def file_index_json_contents_top(): \

    global design

    software_scripts_dir    = os.path.join(federation_root, "software", "scripts")
    CREATE_GPT              = os.path.join(software_scripts_dir, "create-gpt")
    MODEL                   = core_name
    CONFIG                  = "" #FIXME
    design                  = MODEL + "." + CONFIG
    firrtl_build_dtb        = os.path.join(firrtl_build_dir, CONFIG+".dtb")
    firrtl_build_dts        = os.path.join(firrtl_build_dir, CONFIG+".dts")
    firrtl_build_dts_json   = os.path.join(firrtl_build_dir, CONFIG+".json")
    firrtl_build_elaborated_config_json = os.path.join(firrtl_build_dir, "elaborated_config.json")
    firrtl_build_object_model_json      = os.path.join(firrtl_build_dir, CONFIG+".objectModel.json")
    ELF_CONVERT                         = os.path.join(software_scripts_dir, "elf_convert.py")
    firrtl_build_dir                    = firrtl_build_dir
    formal_test_dir                     = os.path.join(federation_root, "software", "tests", "formal")
    ipdelivery_raw_files_dir            = os.path.join(federation_root, "ipdelivery", "UNIVERSAL", "raw_files")
    INPUT_CONFIG                        = os.path.join(federation_root, "configs", "e31.yml")
    memgen_build_dir        = memgen_mybuild
    package_build_dir       = package_mybuild
    project_build_dir       = mybuild_e31_top
    scripts_dir             = os.path.join(federation_root, "scripts")
    SICC                    = os.path.join(software_scripts_dir, "sicc")
    SICC_MEE                = os.path.join(software_scripts_dir, "sicc_mee")
    sim_build_dir           = sim_mybuild
    sim_testbench_v         = os.path.join(federation_root, "vsrc", "sim", TB+".sv")
    metadat_build_dir       = metadata_mybuild
    deputy_dir              = os.path.join(federation_root, "deputy")
    verif_libraries_design_info_c_dir = verif_libraries_design_info_c
    verif_libraies_dir                  = verif_libraries_build_dir
    scripts_vroom_dir                   = os.path.join(scripts_dir, "vroom", "vroom.py")
    sram_info_json                      = "" #CHECKME
    metadata_build_dir                  = metadata_mybuild
    verif_libraries_design_info_tcl             = verif_libraries_design_info_c
    verif_libraries_dir                 = verif_libraries_build_dir

    return \
    formattedStr("//", "File automatically generated by base.mk") + \
    formattedStr("add_size_header", software_scripts_dir+"/add_size_header.py")+\
    formattedStr("bin2denali", software_scripts_dir+"/bin2denali") + \
    formattedStr("bin2hex", software_scripts_dir+"/bin2hex") + \
    formattedStr("create_gpt", CREATE_GPT) + \
    formattedStr("design", design) +\
    formattedStr("device_tree", firrtl_build_dtb) + \
    formattedStr("device_tree_string", firrtl_build_dts) + \
    formattedStr("device_tree_string_json", firrtl_build_dts_json) + \
    formattedStr("elaborated_config_json", firrtl_build_elaborated_config_json) + \
    formattedStr("object_model_json", firrtl_build_object_model_json) + \
    formattedStr("elf_convert", ELF_CONVERT) + \
    formattedStr("federation_dir", federation_root) + \
    formattedStr("file_index_json", file_index_json) + \
    formattedStr("    firrtl_build_dir", firrtl_build_dir) + \
    formattedStr("    formal_test_dir", formal_test_dir) + \
    formattedStr("ipdelivery_raw_files_dir", ipdelivery_raw_files_dir) + \
    formattedStr("input_config", INPUT_CONFIG) + \
    formattedStr("memgen_dir", memgen_build_dir) + \
    formattedStr("package_build_dir", package_build_dir) + \
    formattedStr("project_build_dir", project_build_dir) + \
    formattedStr("run_gdb_self_checking_test", scripts_dir + "/run-gdb-self-checking-test") + \
    formattedStr("sicc", SICC) + \
    formattedStr("sicc_mee", SICC_MEE) + \
    formattedStr("sim_build_dir", sim_build_dir) + \
    formattedStr("sim_testbench_v", sim_testbench_v) + \
    formattedStr("sitest_json_dir", federation_root + "/src/main/sitest") + \
    formattedStr("metadata_build_dir", metadata_build_dir) + \
    formattedStr("deputy_dir", deputy_dir) + \
    formattedStr("verif_libraries_design_info_tcl", verif_design_info_c_dir) + \
    formattedStr("verif_libraries_dir", verif_libraries_dir) + \
    formattedStr("scripts_vroom_dir", scripts_vroom_dir) + \
    formattedStr("sram_info_json_dir", sram_info_json)


def file_index_json_contents_middle():
    software_build_software_compilation_config  = os.path.join(software_mybuild, "software", "compilation_config.json")
    software_bootloaders_dir                    = os.path.join(software_mybuild, "bootloader")
    software_dir                                = software_mybuild
    software_env_dir                            = os.path.join(software_mybuild, "env")
    software_test_dir                           = os.path.join(software_mybuild, "tests")
    TOOLCHAIN_CONFIG                            = os.path.join(federation_root, "software", "configs", "coreip_e3.json")
    toolchain_build_include_dir                 = os.path.join(software_mybuild, "toolchain", "include")
    toolchain_build_linker_dir                  = os.path.join(software_mybuild, "toolchain", "linker")

    return \
    formattedStr("software_compilation_config_json", software_build_software_compilation_config)+\
    formattedStr("software_bootloaders_dir", software_bootloaders_dir) + \
    formattedStr("software_dir", software_dir) + \
    formattedStr("software_test_envs_dir", software_env_dir) + \
    formattedStr("software_test_crt", software_test_dir + "/common/crt.S") + \
    formattedStr("software_test_dir", software_test_dir) + \
    formattedStr("toolchain_config", TOOLCHAIN_CONFIG) + \
    formattedStr("toolchain_include_dir", toolchain_build_include_dir) + \
    formattedStr("toolchain_linker_script_dir", toolchain_build_linker_dir)

#MISSING FPGA PART!!!!!!!!
#NEED TO MIGRATE FROM BASE.MK

def file_index_json_contents_bottom():
    #design = ""#FIXME
    metadata_build_dir = metadata_mybuild

    verilog_module_hier_json            = os.path.join(metadata_build_dir, "module_hierarchy.json")
    verilog_testharness_hier_json       = os.path.join(metadata_build_dir, "testharness_hier.json")
    verilog_build_dir                   = verilog_mybuild
    verilog_build_design_dir            = os.path.join(verilog_build_dir, design)
    verilog_build_design_f              = os.path.join(verilog_build_dir, design+".F")
    verilog_design_vsrcs_f              = "" #FIXME
    verilog_build_assertions_vsrcs_f    = os.path.join(verilog_build_dir, design+".assertions.vsrcs.F")
    verilog_build_coverage_vsrcs_f      = os.path.join(verilog_build_dir, design+".coverage.vsrcs.F")
    verilog_build_grandcentral_vsrcs_f = "" #FIXME
    verilog_build_design_sitest         = os.path.join(verilog_build_dir, design+".sitest")
    verilog_build_testbench_sitest     = "" #FIXME
    verilog_testbench_f                 = ""#FIXME


    return \
    formattedStr("verilog_module_hier_json", verilog_module_hier_json) + \
    formattedStr("verilog_testharness_hier_json", verilog_testharness_hier_json) + \
    formattedStr("verilog_build_dir", verilog_build_dir) + \
    formattedStr("verilog_build_design_dir", verilog_build_design_dir) + \
    formattedStr("verilog_build_design_f", verilog_build_design_f) + \
    formattedStr("verilog_design_vsrcs_f", verilog_design_vsrcs_f) + \
    formattedStr("verilog_build_assertions_vsrcs_f", verilog_build_assertions_vsrcs_f) + \
    formattedStr("verilog_build_coverage_vsrcs_f", verilog_build_coverage_vsrcs_f) + \
    formattedStr("verilog_build_grandcentral_vsrcs_f", verilog_build_grandcentral_vsrcs_f) + \
    formattedStr("verilog_build_design_sitest", verilog_build_design_sitest) + \
    formattedStr("verilog_build_testbench_sitest", verilog_build_testbench_sitest) + \
    formattedStr("verilog_testbench_f", verilog_testbench_f) + \
    "\"verilog_jsons\": [" + \
    package_build_json_dependencies + \
    "null" +\
    "]"
    #FIXME


def gen_file_index(metadata_build_dir):
    global file_index_json
    file_index_json = os.path.join(metadata_build_dir, "file_index.json")

    f       = open(file_index_json, "w")
    f.write("{")
    f.write(file_index_json_contents_top()    + "\n")
    f.write(file_index_json_contents_middle() + "\n")
    f.write(file_index_json_contents_bottom() + "\n")
    f.write("}")
    f.close()


def create_F_file(reference_folder, file_type, F_file_dir):
    srcs = []
    for _, _, files in os.walk(reference_folder):
        for f in files:
            if file_type in f:
                srcs.append(f)

    f = open(F_file_dir, "w")
    for s in srcs: f.write(s + "\n")
    f.close()


def main():



    global federation_root
    global wake_build
    global rocketchip_root
    global firrtl_jar
    global federation_jar
    global firrtl_build_dir
    global verilog_build_conf
    global memgen_build_dir

    wake_build      = ""
    federation_root = ""
    core_name       = "e31" #if not otherwise specify
    if   len(sys.argv) == 3:
            wake_build, federation_root = sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 4:
            wake_build, federation_root, core_name = sys.argv[1], sys.argv[2], sys.argv[3]

    build_dir               = os.path.join(federation_root, "builds", "coreip_" + core_name + "_fcd_try")
    metadata_build_dir      = os.path.join(build_dir, "metadata")
    rocketchip_root         = os.path.join(federation_root, "rocket-chip")
    firrtl_tool_src_root    = os.path.join(rocketchip_root, "firrtl")
    firrtl_jar              = os.path.join(rocketchip_root, "lib", "firrtl.jar")
    firrtl_build_dir        = os.path.join(build_dir, "firrtl")
    verilog_build_dir       = os.path.join(build_dir, "verilog")


    #copy file_index.json --> builds/coreip_e31/metadata/
    os.makedirs(metadata_build_dir)
    os.makedirs(verilog_build_dir)
    original_file_index = os.path.join(federation_root, "builds", "coreip_" + core_name + "_fcd", "metadata", "file_index.json")
    os.system("cp " + original_file_index + " " + metadata_build_dir)
    #gen_file_index(metadata_build_dir) #ACTION

    #copy builds/coreip_e31_fcd/sim -->builds/coreip_e31_fcd_try/
    original_sim_folder = os.path.join(federation_root, "builds", "coreip_" + core_name + "_fcd", "sim")
    os.system("cp -r " + original_sim_folder + " " + build_dir)


    #Input:     build.sbt
    #Output:    firrtl.jar
    mkdir       = os.path.dirname(firrtl_jar) #get dir
    cd          = firrtl_tool_src_root
    cpTarget    = os.path.join(firrtl_tool_src_root, "utils", "bin", "firrtl.jar")
    cpDest      = firrtl_jar
    #do_firrtl_jar(mkdir, cd, cpTarget, cpDest) #ACTION


    #Input:     build.sbt
    #Output:    federation.jar
    federation_jar  = os.path.join(federation_root, "builds", "federation.jar")
    mkdir           = os.path.dirname(federation_jar) #get dir
    cd              = federation_root
    #do_federation_jar(mkdir, cd) #ACTION


    #Wit/Wake/:firrtl           -->   build/coreip/firrtl
    wake_firrtl = os.path.join(wake_build, "firrtl")
    os.system("cp -r " + wake_firrtl + " " + build_dir) #ACTION, since it's copied, could be wrong

    #Wit/Wake:e31.sitest        -->   build/coreip/verilog
    wake_sitest = os.path.join(wake_build, "verilog", core_name + ".sitest")
    os.system("cp " + wake_sitest + " " + verilog_build_dir)

    #Wit/Wake: e31.testbench.sitest --> build/coreip/verilog
    wake_testbn_sitest = os.path.join(wake_build, "verilog", core_name + ".testbench.sitest")
    os.system("cp " + wake_testbn_sitest + " " + verilog_build_dir)



#==========================================================================================
    #verilog_build_conf
        #Wit/Wake:metadata/*   -->   build/coreip/metadata/
    wake_metadata = os.path.join(wake_build, "metadata", "*")
    os.system("cp -r " + wake_metadata + " " + metadata_build_dir)

    #FIRRTL cmd
    wake_CMDLINE_ANNO_FILE      = os.path.join(wake_build, "firrtl", core_name + ".cmdline.anno.json")
    fedr_CMDLINE_ANNO_FILE      = os.path.join(verilog_build_dir, core_name + ".cmdline.anno.json")
        #Wit/Wake:firrtl/e31.cmdline.anno.json      -->     build/verilog/e31.cmdline.anno.json
    os.system("cp " + wake_CMDLINE_ANNO_FILE + " " + fedr_CMDLINE_ANNO_FILE)
    verilog_build_design_dir    = os.path.join(verilog_build_dir, "CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations") #NOTICEME
    verilog_build_testbn_dir    = os.path.join(verilog_build_dir, "CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations.testbench") #NOTICEME
    VERILOG_ANNO_FILES_LIST     = [os.path.join(firrtl_build_dir, core_name + ".anno.json"),
                                    os.path.join(verilog_build_dir, core_name + ".cmdline.anno.json")]
    JAVA                        = "/usr/bin/java "
    FIRRTL_MAX_HEAP             = "20G"
    FIRRTL_MAX_STACK            = "8M"
    FIRRTL_MAIN                 = "firrtl.Driver"
    MODEL                       = "CoreIPSubsystemAllPortRAMTestHarness"
    verilog_build_conf          = os.path.join(verilog_build_dir, \
                                    "CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations.conf")
    FIRRTL                      = JAVA + "-Xmx" + FIRRTL_MAX_HEAP + " -Xss" + \
                                    FIRRTL_MAX_STACK +  " -cp " + federation_jar + " " + FIRRTL_MAIN
    VERILOG_FIRRTL_ARGS         = "--infer-rw" + " " + MODEL + " "\
                                  "--repl-seq-mem -c:" + MODEL + ":-o:" + verilog_build_conf + " " +\
                                  "--split-modules -tn " + MODEL + " " +\
                                  "-td " + verilog_build_design_dir + " "  + \
                                  "-fct " + ",".join(FIRRTL_TRANSFORMS) + " " + \
                                  " -faf " + " -faf ".join(VERILOG_ANNO_FILES_LIST) + " -ll info "
    FIRRTL_CMDLINE              = FIRRTL + " -i " + os.path.join(firrtl_build_dir, core_name + ".pb") + \
                                    " -X verilog " + VERILOG_FIRRTL_ARGS
        #Input:     e31.cmdline.anno.json
        #Output:    CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations.conf && .V files
    #os.system(FIRRTL_CMDLINE) #ACTION
    print(FIRRTL_CMDLINE)
#==============================================================================================

    wake_verilog_design_folder   = os.path.join(wake_build, "verilog", "design", "*")
    wake_verilog_testbn_folder   = os.path.join(wake_build, "verilog", "testbench", "*")
    wake_firrtl_memcon_file      = os.path.join(wake_build, "firrtl",  "mems.conf")
    verilog_build_dir_conf       = os.path.join(verilog_build_dir, \
                                    "CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations.conf")

    os.makedirs(verilog_build_design_dir)
    os.makedirs(verilog_build_testbn_dir)
    #Wit/Wake: verilog/design       -->         build/coreip/verilog/CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations
    os.system("cp -r " + wake_verilog_design_folder + " " + verilog_build_design_dir)
    #Wit/Wake: verilog/testbench    -->         build/coreip/verilog/CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations.testbench
    os.system("cp -r " + wake_verilog_testbn_folder + " " + verilog_build_testbn_dir)

    os.system("cp -r " + wake_firrtl_memcon_file + " " + verilog_build_dir_conf)

    _vsrcs_F             = os.path.join(verilog_build_dir, \
                                "CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC." + core_name + ".vsrcs.F")
    _F                   = os.path.join(verilog_build_dir, \
                                "CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC." + core_name + ".F")
    _vsrcs_testbn_F      = os.path.join(verilog_build_dir, \
                                "CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC." + core_name + ".testbench.vsrcs.F")
    _testbn_F            = os.path.join(verilog_build_dir, \
                                "CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC." + core_name + ".testbench.F")



    os.system("touch " + _vsrcs_F)
    os.system("touch " + _vsrcs_testbn_F)
    os.system("touch " + _F)
    os.system("touch " + _testbn_F)

    #Input:     build/coreip/verilog/CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations/.v
    #Input:     build/coreip/verilog/CoreIPSubsystemAllPortRAMTestHarness.SiFiveCoreDesignerAlterations.testbench/.v

    #Output:    build/coreip/verilog/CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC.e31.vsrcs.F
    #Output:    build/coreip/verilog/CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC.e31.F
    #Output:    build/coreip/verilog/CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC.e31.testbench.vsrcs.F
    #Output:    build/coreip/verilog/CoreIPSubsystemAllPortRAMVerificationTestHarnessWithDPIC.e31.testbench.F
    create_F_file(verilog_build_design_dir, "", _vsrcs_F)
    create_F_file(verilog_build_testbn_dir, "", _vsrcs_testbn_F)
    create_F_file(verilog_build_design_dir, "", _F)
    create_F_file(verilog_build_testbn_dir, "", _testbn_F)

    #VROOM
    #create verif/libraries/design_info c, sv, tcl
    #prepare directory for vroom.py
    verif_build_dir                    = os.path.join(build_dir, "verif")
    verif_libraries_build_dir          = os.path.join(verif_build_dir, "libraries")
    verif_libraries_design_info_c      = os.path.join(verif_libraries_build_dir, "design_info", "c")
    verif_libraries_design_info_sv     = os.path.join(verif_libraries_build_dir, "design_info", "sv")
    verif_libraries_design_info_tcl    = os.path.join(verif_libraries_build_dir, "design_info", "tcl")
    os.makedirs(verif_libraries_design_info_c)
    os.makedirs(verif_libraries_design_info_sv)
    os.makedirs(verif_libraries_design_info_tcl)

    #Input:     build/coreip/firrtl/e31.objectModel.json
    #Input:     build/coreip/firrtl/e31.AHBPortRAMSlave_AddressMap_1.json
    #Input:     build/coreip/firrtl/e31.AHBPortRAMSlave_AddressMap_2.json

    #Output:    build/coreip/verif/libraries/design_info/c/*
    #Output:    build/coreip/verif/libraries/design_info/sv/*
    #Output:    build/coreip/verif/libraries/design_info/tcl/*
    vroom_sram_info_arg     = "" #FIXME
    vroom_exe               = os.path.join(federation_root, "scripts", "vroom", "vroom.py")
    _object_model           = os.path.join(firrtl_build_dir, core_name + ".objectModel.json")
    test_mem                = subprocess.check_output("cd " + firrtl_build_dir + " && find . | grep AHBPortRAMSlave_AddressMap"\
                                , shell=True)

    test_mem_arr            = test_mem.decode("utf-8").rstrip("\n").split("\n")
    test_mem_absPath_arr    = map(lambda x: os.path.join(firrtl_build_dir, x), test_mem_arr)
    test_mem_as_arg         = map(lambda x: " --test-memory-json " + x, test_mem_absPath_arr)
    test_mem_partial_cmd    = " ".join(test_mem_as_arg)
    c_partial_cmd           = " --gen-c --ovrd-c-out-dir=" + verif_libraries_design_info_c + " " + vroom_sram_info_arg
    sv_partial_cmd          = " --gen-sv --ovrd-sv-out-file=" + verif_libraries_design_info_sv + "/sifive_amba_system_config.sv"
    tcl_partial_cmd         = " --gen-tcl --ovrd-tcl-out-file=" + verif_libraries_design_info_tcl + "/ominfo.tcl"
    full_vroom_cmd          = vroom_exe + " " + _object_model + c_partial_cmd \
                            + sv_partial_cmd + tcl_partial_cmd + test_mem_partial_cmd
    os.system(full_vroom_cmd)
    print(full_vroom_cmd)



    #MEMGEN
        #preMemGen
        #create memgen directory
    memgen_build_dir = os.path.join(build_dir, "memgen")
    os.makedirs(memgen_build_dir)

    #dpi_raminfo
    #Input:     /sifive/vip/ieee/1800-2017/include
    #Input:     build/coreip/verif/libraries/design_info/c/dpi_raminfo.c

    #Output:    build/coreip/memgen/dpi_raminfo.o
    CXX         = "/sifive/tools/gcc/7.2.0/bin/g++"
    svdpi_dir   = "/sifive/vip/ieee/1800-2017/include"
    cmd         = CXX + " -c -Wall -Wno-unused-variable -I" + svdpi_dir + " " + \
                    os.path.join(verif_libraries_design_info_c, "dpi_raminfo.c") + " -o " + \
                    os.path.join(memgen_build_dir, "dpi_raminfo.o")
    os.system(cmd)

    #mem_gen_dpi
    #Input:     federation/vlsi-mem/mem_gen_dpi.cpp
    #Input:     build/coreip/verif/libraries/design_info/tcl/*

    #Ouput:     build/coreip/memgen/mem_gen_dpi.o
    vlsi_mem_dir = os.path.join(federation_root, "vlsi-mem")
    cmd         = CXX + " -c -Wall -std=c++17 -I"\
                    +svdpi_dir + " -I" + verif_libraries_design_info_tcl \
                    + " " +  os.path.join(vlsi_mem_dir, "mem_gen_dpi.cpp") \
                    + " -o " + os.path.join(memgen_build_dir, "mem_gen_dpi.o")
    os.system(cmd)

    #dpi_mem_api
    #Input:     build/coreip/memgen/mem_gen_dpi.o
    #Input:     build/coreip/memgen/dpi_raminfo.o

    #Output:    build/coreip/memgen/mem_gen_dpi.a
    cmd = "ar -r " + os.path.join(memgen_build_dir, "mem_gen_dpi.a") + " " +\
            os.path.join(memgen_build_dir, "mem_gen_dpi.o") + " " +\
            os.path.join(memgen_build_dir, "dpi_raminfo.o")
    os.system(cmd)

        #realMemGen
        #Output:    build/coreip/memgen/memalpha.json
        #Output:    build/coreip/memgen/rams.v
    INTERACTIVE                     = False
    MEMORY_COMPILER_SIZE_THRESHOLD  = str(0)
    #PREPEND_MEMORY_WRAPPER          = False #CHECKME
    #APPEND_MEMORY_WRAPPER           = False #CHECKME
    #MEMORY_MODULE_SKIP_LIST         = False #CHECKME
    memgen_build_rams_v             = os.path.join(memgen_build_dir, core_name + ".rams.v")
    memgen_conf_json                = os.path.join(federation_root, "vlsi-mem", "mem_gen_config.json")
    memgen_build_memalpha_meta      = os.path.join(memgen_build_dir, core_name + ".memalpha.json")
    MEM_GEN                         = os.path.join(federation_root, "vlsi-mem/vlsi_mem_gen.behavioral-DPI")
    interactive                     = " --interactive " if INTERACTIVE is True else  " "
    compiler_size                   = " --compiler-size-threshold " + MEMORY_COMPILER_SIZE_THRESHOLD
    iconf                           = " --iconf " + verilog_build_conf
    param_json                      = " --param_json " + memgen_conf_json
    oconf                           = " --oconf " + memgen_build_memalpha_meta
    wrper                           = " --wrapper " + memgen_build_rams_v
    #prepend_mem                     = (" --prepend-verilog-source " + PREPEND_MEMORY_WRAPPER) if \
    #                                    PREPEND_MEMORY_WRAPPER is True else " "
    #appned_mem                      = (" --append-verilog-source " + APPEND_MEMORY_WRAPPER ) if \
    #                                    APPEND_MEMORY_WRAPPER is True  else " "
    #module_skip_list                = (" --skip-list" + MEMORY_MODULE_SKIP_LIST) if \
    #                                    MEMORY_MODULE_SKIP_LIST is True else " "
    full_cmd                        =\
                                        MEM_GEN + interactive + compiler_size + iconf + param_json + \
                                        oconf + wrper
    os.system(full_cmd)



    #memgen_build_rams_json
    #Input:     build/coreip/memgen/e31.memalpha.json

    #Output:    build/coreip/memgen/e31.rams.json
    memgen_build_rams_json          = os.path.join(memgen_build_dir, core_name + ".rams.json")
    MEMALPHA                        = os.path.join(federation_root, "memory-alpha", "bin", "memalpha")
    memgen_macro_dir                = "/work/memory/staging"
    cmdline                         = MEMALPHA \
                                        + " sitest -d " + memgen_macro_dir \
                                        + " --vlib " + memgen_build_rams_v \
                                        + " " + memgen_build_rams_json \
                                        + " < " + memgen_build_memalpha_meta
    os.system(cmdline)


    #verif_dir_built
    #Input:     build/coreip/firrtl/e31.json
    #Input:     build/coreip/firrtl/e31.AHBPortRAMSlave_AddressMap_1.json
    #Input:     build/coreip/firrtl/e31.AHBPortRAMSlave_AddressMap_2.json
    #Input:     federation/configs/e31.yml

    #Output:    build/coreip/firrtl/elaborated_config.json
    firrtl_build_elaborated_config_json = os.path.join(firrtl_build_dir, "elaborated_config.json")
    firrtl_build_dts_json           = os.path.join(firrtl_build_dir, core_name + ".json") #NOTICEME
    INPUT_CONFIG                    = os.path.join(federation_root, "configs", core_name + ".yml")
    BUILD_ELABORATED_CONFIG_JSON    = os.path.join(federation_root, "scripts", "build-elaborated-config-json.py")
    #I'm missing one line for the following cmd, but in this case it doesn't matter
    BUILD_cmd                       = BUILD_ELABORATED_CONFIG_JSON +" --dts-json " + firrtl_build_dts_json + " " + \
                                        test_mem_partial_cmd + " " + \
                                        "--input-config=" + INPUT_CONFIG + \
                                        " --output " + os.path.join(firrtl_build_dir, "elaborated_config.json")
    os.system(BUILD_cmd)



    #software_build_software_compilation_config
    #Input:     some variables

    #Output:    build/coreip/software/compilation_config.json
    software_build_dir                          = os.path.join(build_dir, "software")
    os.makedirs(software_build_dir)
    software_build_software_compilation_config  = os.path.join(software_build_dir, "compilation_config.json")
    XCCMODEL = "medlow"
    TEST_ENV = "default"
    f = open(software_build_software_compilation_config, "w")
    f.write("{" + "\"code_model\"" + ":" + XCCMODEL + " " + "\"test_env\"" + ":" + TEST_ENV + "}")
    f.close()


    #toolchain
        #toolchain_build_built
        #Input:     federation/software/configs/coreip_e3.json
        #Input:

        #Output:
    software_dir                = os.path.join(federation_root, "software")
    software_toolchain_dir      = os.path.join(software_dir, "toolchain")
    toolchain_build_toolchain   = os.path.join(software_toolchain_dir, "build_toolchain.py")
    TOOLCHAIN_CONFIG            = os.path.join(software_dir, "configs", "coreip_e3.json") #FIXME, not always coreip_e3.json
    firrtl_build_iof_json       = os.path.join(firrtl_build_dir, core_name + ".iof.json")
    toolchain_build_dir         = os.path.join(build_dir, "software", "toolchain")

    cmdline                     = toolchain_build_toolchain     + " "\
                                    "--extra-input-config "     + TOOLCHAIN_CONFIG + " " \
                                    "--iof-input-config "       + firrtl_build_iof_json + " "\
                                    "--elaborated-config-json " + firrtl_build_elaborated_config_json + " " \
                                    "-o "                       + toolchain_build_dir
    os.system(cmdline)

        #toolchain_meminfo_built
        #Input:     build/coreip/firrtl/elaborated_config.json
        #Output:
    software_scripts_dir        = os.path.join(software_dir, "scripts")
    BUILD_MEMINFO_LIB           = os.path.join(software_scripts_dir, "build-meminfo-lib")
    toolchain_build_meminfo_dir = os.path.join(toolchain_build_dir, "libraries", "meminfo")
    cmdline                     = BUILD_MEMINFO_LIB + " "\
                                    "--elaborated-config-json " + firrtl_build_elaborated_config_json + " " \
                                    "-o " + toolchain_build_meminfo_dir
    os.system(cmdline)

        #toolchain_hartinfo_built
    BUILD_HARTINFO_LIB              = os.path.join(software_scripts_dir, "build-hartinfo-lib")
    toolchain_build_hartinfo_dir    = os.path.join(toolchain_build_dir, "libraries", "hartinfo")
    cmdline                     = BUILD_HARTINFO_LIB + " " + \
                                    "--elaborated-config-json " +  firrtl_build_elaborated_config_json + " " \
                                    "-o " + toolchain_build_hartinfo_dir

if __name__== "__main__":
    main()
