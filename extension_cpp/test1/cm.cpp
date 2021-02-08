/**
 * from example: https://zhuanlan.zhihu.com/p/76058539
 */
#include <iostream>
#include <string>
using namespace std;

#ifdef __cplusplus
extern "C"{
#endif

int cm(int n){
    int cm=0;
    int i;
    for(i=1;i<=n;++i){
        cm += i;
        cm -= i;
    }
    return(cm);
}

#ifdef __cplusplus
}
#endif