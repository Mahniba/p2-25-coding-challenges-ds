package com.test;

public class challenge_33 {
    public static String sum(String n){
        StringBuilder temp = new StringBuilder();
        String before = "";
        String after="";
        int sum = 0;
        for (int i=0; i<n.length(); i++){
            after = Character.toString(n.charAt(i));
            before = after;
            if (after.equals(",")){
                sum += Integer.parseInt(temp.toString());
                temp = new StringBuilder();
            }
            else {
                temp.append(before);
            }
        }
        sum += Integer.parseInt(temp.toString());
        return Integer.toString(sum);
    }
}
