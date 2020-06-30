#include <math.h>
int _is_prime(int i)
{
    int test;
    for(test=2;test<=sqrt(i);test++)
    {
        if(i%test==0)
        {
            return 0;
        }
    }
    return 1;
}