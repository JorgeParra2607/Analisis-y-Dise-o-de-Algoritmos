#include <stdio.h>

int sqrt_binary_search(int x);

int main(){

    int x;
    printf("Ingresa un numero: ");
    scanf("%d", &x);
    printf("\nLa raiz cuadrada de %d es %d\n", x, sqrt_binary_search(x));

return 0;
}

int sqrt_binary_search(int x){

    //Casos Base
    if (x == 0 || x == 1){

        return x;
    }

    int l = 0, r = x / 2;
    int ans;

    while (l <= r) {
        int mid = l + (r - l) / 2;

        if ((long long)mid * mid <= x){
            ans = mid;
            l = mid + 1;
        }

        else{
            r = mid - 1;
        }
    }
    return ans;
}
