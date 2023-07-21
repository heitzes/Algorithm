class Solution {
    public int solution(int n) {
        int answer = 1;
        int factorial = 1;
        while (factorial * (answer+1) <= n) {
            answer += 1;
            factorial *= answer;
        }
        
        return answer;
    }
}