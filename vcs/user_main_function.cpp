////////////////////////////////////////////////////////////
// create systemc only module
// compile sysc module with  sysscan 
////////////////////////////////////////////////////////////

#include "systemc.h"
#include "svdpi.h"
#include "stdio.h"
//#include "systemc_user.h"

int global_flag=0xbeef;

void sample2(int a)
{
  printf ("hello world from %s in=%d\n", __FUNCTION__, a);

}


SC_MODULE(standalone)
{

  SC_CTOR(standalone) 
  {
    static int cnt=0;
    printf ("hello world from SC standalone module %s line %d cnt=%d\n",__FILE__,__LINE__,cnt);
//assert(0);

    assert (++cnt<2 && "how can we call this twice???");
    //SC_THREAD(mythread) sensitive << clk;
    SC_THREAD(mythread);
  }

  void mythread();
  void end_of_elaboration()
  {
    printf ("hello world from SC standalone module %s line %d \n",__FUNCTION__,__LINE__);
  }
  void before_end_of_elaboration()
  {
    printf ("hello world from SC standalone module %s line %d \n",__FUNCTION__,__LINE__);
  }

};



void standalone::mythread()
{
  int i;

  for (i=0; i<20; i++)
  {
    printf ("hello world from SC standalone module %s line %d i=%d\n",__FILE__,__LINE__,i);
    wait(1,SC_NS);
  }
  printf ("hello world from SC %s standalone module line %d \n",__FILE__,__LINE__);
}


standalone standalone("alone");

int user_main_function (int , char **)
{
  static int cnt=0;

  printf ("calling from %s cnt=%d\n",__FUNCTION__, cnt);
  assert (++cnt<2 && "how can we call this twice???");

}

extern "C" int sc_main_register(int (*) (int , char **));

static int my_sc_main = sc_main_register(user_main_function);



