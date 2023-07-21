class Solution {
    public int solution(int a, int b) {
        int answer = 1;
        int mini = a > b ? b : a;
        int maxi = a > b ? a : b;
        for (int i=2; i<=mini; i++) {
            if (mini % i == 0 && maxi % i == 0) {
                mini /= i;
                maxi /= i;
            }
        }
        if (a > b) {
            while (mini > 1) {
                if (mini % 2 == 0) {
                    mini /= 2;  
                    continue;
                } break;
            }
            while (mini > 1) {
                if (mini % 5 == 0) {
                    mini /= 5;   
                    continue;
                } break;
            }
            if (mini != 1) answer = 2;
            
        } else {
            while (maxi > 1) {
                if (maxi % 2 == 0) {
                    maxi /= 2;   
                    continue;
                } break;
            }
            while (maxi > 1) {
                if (maxi % 5 == 0) {
                    maxi /= 5; 
                    continue;
                } break;
            }
            if (maxi != 1) answer = 2;
        }
        
        return answer;
    }
}