class Solution {
    public String solution(String s) {
        String answer = "";
        String[] words = s.split(" ");
        boolean flag = false;
        if (s.charAt(s.length()-1) == ' ') {
            flag = true;
        }
        for (String word : words) {
            if (word.length() <= 0) {
                answer += " ";
                continue;
            };
            char ch = word.charAt(0);
            if (! ('0'<=ch && ch<='9')) {
                StringBuffer sb = new StringBuffer(word.toLowerCase());
                sb.setCharAt(0, (char) (sb.charAt(0) - 32));
                answer += sb + " ";
            } else {
                answer += word.toLowerCase() + " ";
            }
        }
        if (flag) {
            return answer.substring(0, answer.length());
        }
        return answer.substring(0, answer.length()-1);
    }
}