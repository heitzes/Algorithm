import java.util.*;
class Solution {
    public int[][] solution(int[] num_list, int n) {
        int leng = num_list.length / n;
        int[][] answer = new int[leng][];
        for (int i=0; i<leng; i++) {
            answer[i] = Arrays.copyOfRange(num_list, i*n, Math.min(num_list.length, i*n + n));
        }
        
        return answer;
    }
}