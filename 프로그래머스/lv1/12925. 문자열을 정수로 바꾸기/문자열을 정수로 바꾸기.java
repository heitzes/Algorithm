class Solution {
    public int solution(String s) {
        int answer = 0;
        int flag = 1;
        if (s.charAt(0) == '-') {
            flag = -1;
        }
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == '-' | s.charAt(i) == '+') continue;
            answer += (s.charAt(i) - '0') * Math.pow(10, s.length()-1-i);
        }
        
        return answer * flag;
    }
}