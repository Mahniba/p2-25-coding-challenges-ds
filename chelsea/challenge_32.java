package com.test;

public class challenge_32 {
    public static StringBuilder wordCapitalise(String text){
        String before = " ";
        String after = "";
        StringBuilder ret = new StringBuilder();
        for (int i=0; i<text.length(); i++){
            after = Character.toString(text.charAt(i));
            if (!after.equals(" ") && before.equals(" ")){
                ret.append(Character.toUpperCase(text.charAt(i)));
            }
            else
                ret.append(Character.toString(text.charAt(i)));
            before = after;
        }
        return ret;
    }
}
