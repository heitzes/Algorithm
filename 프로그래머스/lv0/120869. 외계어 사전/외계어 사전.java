import java.util.*;
class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;
        Loop1 : for (String word : dic) {
            for (String s : spell) {
                if (word.indexOf(s)==-1) continue Loop1;
            }
            answer = 1;
        }
        
        return answer;
    }
}