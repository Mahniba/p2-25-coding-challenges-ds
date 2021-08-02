package com.test;

public class challenge_27 {
    public static int[] distinct(int[] arr){
        int[] ret = new  int[arr.length];
        int dis = 0, ind = 0;
        boolean test;
        while (ind != arr.length){
            test = true;
            for (int i: arr){
                if (dis == i){
                    test = false;
                    break;
                }
            }
            if (test){
                ret[ind] = dis;
                ind ++;
            }
            dis ++;
        }
        return ret;
    }
}
