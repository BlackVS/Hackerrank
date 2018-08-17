#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

#define MINV 1
#define MAXV 1000000
#define MINN 1
#define MAXN 500000
    
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int main() {
    int n; 
    int minA=MAXV+1, maxA=MINV-1;
    int minB=MAXV+1, maxB=MINV-1;
    
    scanf("%i", &n);

    bool *pA = (bool*)calloc(MAXV+1,sizeof(bool));
    int a;
    for (int i = 0; i < n; i++) {
       scanf("%i",&a);
       pA[a]=true;
       minA=MIN(minA,a);
       maxA=MAX(maxA,a);
    }

    bool *pB = (bool*)calloc(MAXV+1,sizeof(bool));
    int b;
    for (int i = 0; i < n; i++) {
       scanf("%i",&b);
       pB[b]=true;
       minB=MIN(minB,b);
       maxB=MAX(maxB,b);
    }
    
    int res=0;
    int maxG=MIN(maxA,maxB);
    for(int g=maxG; g>=1; g--)
    {
        int ma=(maxA/g)*g;
        int ra=0;
        int rb=0;
        while(ma>=minA){
            if(pA[ma]){
                ra=ma;
                break;
            }
            ma-=g;
        }
    
        int mb=(maxB/g)*g;
        while(mb>=minB){
            if(pB[mb]){
                rb=mb;
                break;
            }
            mb-=g;
        }
        if(ra&&rb){
            res=ra+rb;
            break;
        }
    }
    printf("%d",res);
    free(pA);
    free(pB);
    return 0;
}
