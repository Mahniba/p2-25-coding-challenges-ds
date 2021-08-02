package com.test;

public class challenge_26 {
    public static int[] exclusive(int[] arr1, int[] arr2){
        int size = arr1.length;
        boolean test;
        for (int i: arr1){
            for (int j: arr2){
                if (i == j)
                    size -= 1;
            }
        }
        int[] ret = new int[size];
        size = 0;
        for (int i: arr1){
            test = true;
            for (int j: arr2){
                if (i == j){
                    test = false;
                }
            }
            if (test){
                ret[size] = i;
                size ++;
            }
        }
        return ret;
    }
}
