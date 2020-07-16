///////////////////////////////////////////////////////////////////////////
// module code body
///////////////////////////////////////////////////////////////////////////

//#include "systemc.h"
#include "systemc_user.h"
#include "stdio.h"
#include "stdlib.h"
#include "sc_top.h"


extern int global_flag;


void sc_top::mythread()
{
  int i;

  printf ("hello world from SC module with verilog wrapper %s line %d\n",__FILE__,__LINE__);
  for (i=0; i<20; i++)
  {
    printf ("hello world %s line %d\n",__FILE__,__LINE__);
    wait();
  }
  printf ("hello world from SC %s line %d\n",__FILE__,__LINE__);
  printf ("my global extern: %x \n",global_flag);
}






