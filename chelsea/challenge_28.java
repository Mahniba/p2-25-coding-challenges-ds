package com.test;

public class challenge_28 {
    public static int[] sum_100_prime(){
        int[] sums = new  int[100], primes = new int[]{2,3,5,7,11,13,17};
        boolean test;
        int num = 2, ind = 0, sum = 0;
        while (ind != 100){
            test = true;
            for (int prime: primes){
                if (num == prime){
                    break;
                }
                if (num % prime == 0){
                    test = false;
                    break;
                }
            }
            if (test){
                sum += num;
                sums[ind] = sum;
                ind ++;
            }
            num ++;
        }
        return sums;
    }
}
