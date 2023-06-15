class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<=n; i++) {
            int cnt = count(i);
            if (cnt >= 3) answer += 1;
        }
        return answer;
    }
    
    public int count(int n) {
        int cnt = 0;
        for (int i=1; i<=n; i++) {
            if (n % i == 0) cnt += 1;
        }
        return cnt;
    }
    
}