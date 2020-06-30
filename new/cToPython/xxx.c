#include<stdio.h>
long long jie(long long n){
    long long i;
    long long sum=1;
    for(i = 2;i<=n;i++){
        sum*=i;
    }
    return sum;
}