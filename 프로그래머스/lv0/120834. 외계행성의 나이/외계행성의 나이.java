class Solution {
    public String solution(int age) {
        String answer = "";
        for (char ch : (""+age).toCharArray()) {
            answer += ((char)(Integer.parseInt(""+ch)+'a'));
        }
        return answer;
    }
}