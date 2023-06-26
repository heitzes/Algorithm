import java.util.*;
class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "";
        Map<String, String> map = new HashMap<>();
        for (String[] info : db) {
            map.put(info[0], info[1]);
        }
        return map.get(id_pw[0]) == null ? "fail" : (map.get(id_pw[0]).equals(id_pw[1]) ? "login" : "wrong pw");
    }
}