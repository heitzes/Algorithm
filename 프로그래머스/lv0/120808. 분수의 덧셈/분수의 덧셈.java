class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        numer1 = numer1 * denom2;
        numer2 = numer2 * denom1;
        denom2 = denom2 * denom1;
        
        int numer = numer1 + numer2;
        int denom = denom2;
        int maxi = 0;
        for (int i = Math.min(numer, denom); i > 1; i--) {
            if ((numer % i == 0) && (denom % i == 0)) {
                maxi = i;
                break;
            }
        }
        
        if (maxi != 0) {
            answer[0] = numer / maxi;
            answer[1] = denom / maxi;
        } else {
            answer[0] = numer;
            answer[1] = denom;
        }
        
        return answer;
    }
}