import java.util.*;

class Solution {
    public double solution(int[] arr) {
        int size = arr.length;
        double answer = 0;
        for(int i : arr) {
            answer += i;
        }
        return answer / size;
    }
}