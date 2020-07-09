

#ifndef TOP_H
#define TOP_H

#include "systemc_user.h"

SC_MODULE(sc_top)
{
  sc_in_clk clk;

  SC_CTOR(sc_top) 
  {
    printf ("hello world from SC %s line %d\n",__FILE__,__LINE__);
    SC_THREAD(mythread)
      sensitive << clk;
  }

  void mythread();

};


#endif

