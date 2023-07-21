class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n%2==1) {
            answer = (int)Math.pow(n/2+1, 2);
        } else {
            for (int i=2; i<=n; i+=2) {
                answer += (int)Math.pow(i, 2);
            }
        }
        return answer;
    }
}