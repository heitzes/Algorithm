import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(n);
        while (n != 1) {
            if (n % 2==0) {
                n /= 2;
            } else {
                n = 3*n + 1;
            }
            arr.add(n);
        }
        int[] answer = arr.stream()
	        .mapToInt(Integer::intValue)
    	    .toArray();
        return answer;
    }
}