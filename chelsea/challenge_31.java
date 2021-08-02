package com.test;

public class challenge_31 {
    public static int wordCount(String text){
        int sym = text.length(), count = 0;
        String before = " ", after = "";
        for (int i=0; i<sym; i++){
            after = Character.toString(text.charAt(i));
            if (!after.equals(" ") && before.equals(" ")){
                count += 1;
            }
            before = after;
        }
        return count;
    }
}
