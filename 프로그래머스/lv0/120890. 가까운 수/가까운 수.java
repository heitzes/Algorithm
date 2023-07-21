import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        Arrays.sort(array);
        int mini = 101;
        for(int i=0; i<array.length; i++) {
            if (Math.abs(n-array[i]) < mini) {
                mini = Math.abs(n-array[i]);
                answer = i;
            }
        }
        return array[answer];
    }
}