
echo BASH

#######################################################################
# notes: 
#        gcc 4.8.3 used
#        gcc 6.2 with systemc 2.3.2 recommended
#4.8.3/     4.9.4/     7.2.0/     9.2.0/     downloads/ 
#######################################################################

echo "This is a BASH script, you should source "
echo " 1      : module load 2015 version vcs"
echo " 2      : module load synopsys generic "
echo " 4      : module load 2019 version vcs"
echo " 16     : clean "
echo " 256    : gcc compile "
echo " 512    : vcs compile child module "
echo " 1024   : syscan on sc_top module "
echo " 2048   : vcs compile"

childdir=/home/ahung/union/vcs/child

sysch=/sifive/tools/synopsys/vcs/Q-2020.03-SP1/include/systemc231

if [ $(($# )) -ne 0 ]; then
  cmdarg=$1
else
  cmdarg=131072
  cmdarg=3858
fi

gccpath=/sifive/tools/gcc/4.8.3/bin/g++
gccpath=/scratch/ahung/gcc/gcc-6.2.0/bin/g++
echo cmdarg: $cmdarg

$gccpath -v

if [ $(($cmdarg & 1)) -ne 0 ]; then
  module unload synopsys/vcs
  module load synopsys/vcs/K-2015.09-SP2
fi

if [ $(($cmdarg & 2)) -ne 0 ]; then
  module unload synopsys/vcs
  module load synopsys/vcs/Q-2020.03-SP1 
fi

if [ $(($cmdarg & 4)) -ne 0 ]; then
  module unload synopsys/vcs
  module load synopsys/vcs/P-2019.06-SP2
fi


if [ $(($cmdarg & 8)) -ne 0 ]; then
  gccpath=/sifive/tools/gcc/7.2.0/bin/g++
fi


# to do all this vcs stuff 917504
if [ $(($cmdarg & (16))) -ne 0 ]; then
  echo setup SC module stuff, clean .......
#  module load gcc/gcc/4.8.3
  module list
  echo which gcc:
  which gcc
  gcc -v
  echo forced gcc path:
  echo $gccpath
  
  rm -rf simv*
  rm -rf AN*
  rm -rf csrc
  rm -rf sysc
  rm -rf child
  rm -rf *so
fi

# note: we need fPIC
if [ $(($cmdarg & (256))) -ne 0 ]; then
  echo ...........................
  echo do our gcc compile
#  g++ -v
  sleep 2
  $gccpath -fPIC -shared sysc_sample.cpp -o ./sctest.so 
  $gccpath -fPIC -shared -I$sysch/.. -I$sysch user_main_function.cpp sysc_sample.cpp -o ./scsim.so 
  echo do our gcc compile done

fi



commonverilog="-timescale=1ns/10ps"

if [ $(($cmdarg & (512))) -ne 0 ]; then
  echo vcs: make child module stuff.......
  sleep 2

  vcs -sverilog -Mdir=$childdir $commonverilog ./childmod.v 
  
  echo make child module done
fi

# we can do 655360
if [ $(($cmdarg & (1024))) -ne 0 ]; then
  echo proof of concept SC stuff stuff.......

  echo doing syscan, which is wrapper generation
  sleep 2
  syscan -Mdir=$childdir -cpp $gccpath -sysc=2.3.1 -shared -full64 ./sc_top.cpp:sc_top

  echo syscan done
fi

if [ $(($cmdarg & (2048))) -ne 0 ]; then

  echo ...........................
  echo making simv with vcs
  echo mlib is where to find external modules
  echo mdir is where put generated files
  vcs -Mlib=$childdir -Mdir=$childdir/../csrc ./childmod.v -sysc=2.3.1 $commonverilog  -top top -sverilog user_main_function.cpp ./sctest.so -cpp $gccpath  ./top.v
  module unload gcc

fi


if [ $(($cmdarg & (4096))) -ne 0 ]; then

  echo ...........................
  echo making simv2 with vcs

fi

if [ $(($cmdarg & (65536))) -ne 0 ]; then

  echo ...........................
  echo various info............. 
  echo \-Mlib=$childdir \-Mdir=$childdir/../csrc -sysc=2.3.1 $childdir/../scsim.so -cpp $gccpath  

module list
echo gccpath: $gccpath

fi



