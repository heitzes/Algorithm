import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n+1];
        arr[1] = 1;
        for (int i=2; i<=n; i++) {
            for (int k=arr[i-1]+1; ; k++) {
                if (k % 3 != 0 && (""+k).indexOf("3") == -1) {
                    arr[i] = k;
                    break;
                }
            }
        }
        return arr[n];
    }
}