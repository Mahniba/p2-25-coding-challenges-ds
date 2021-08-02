package com.test;

public class challenge_34 {
    public static String[] wordArray(String text){
        String before = " ", after = "", temp = "";
        int size = 0, position = 0;
        for (int i=0; i<text.length(); i++){
            after = Character.toString(text.charAt(i));
            if (after.equals(" ") && !before.equals(" "))
                size ++;
            before = after;
        }
        before = " ";
        String[] ret = new String[size + 1];
        for (int i=0; i<text.length(); i++){
            after = Character.toString(text.charAt(i));
            if (after.equals(" ") && !before.equals(" ")) {
                ret[position] = temp;
                position ++;
                temp = "";
            }
            else {
                temp += Character.toString(text.charAt(i));
            }
            before = after;
        }
        ret[position] = temp;
        return ret;
    }
}
