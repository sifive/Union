////////////////////////////////////////////////////////////
// contain one dpi
// 
////////////////////////////////////////////////////////////

//#include "systemc.h"
#include "assert.h"
#include "stdio.h"

class standalone_class
{
  
public:
  standalone_class()
  {
    static int cnt=0;
    printf ("hello world from standalone SC module %s in=%d this=%p cnt=%d\n", __FUNCTION__, __LINE__, this,cnt); 
    assert (++cnt<2 && "how can we call this twice???");
  }


} stand;

extern "C" {
void sample_dpi(int a)
{
  printf ("hello world from %s in=%d\n", __FUNCTION__, a);

}
}

