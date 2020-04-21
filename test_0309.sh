rm -rf /scratch/ericc/work/make_fed_test/builds/coreip_e31_fcd_try
rm -rf /scratch/ericc/work/make_fed_test/rocket-chip
/scratch/ericc/work/make_fed_test/scripts/quick-submodule-update
python3 replaceSim_0309.py /home/ericc/work/wake_2020_04_20/workspace/build/product-coreip-sifive/e31 /home/ericc/work/make_fed_test /home/ericc/work/make_fed_test/mk/base_configs/coreip_e31_fcd.mk

