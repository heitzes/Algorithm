import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        int[] answer = {};
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (char ch : my_string.toCharArray()) {
            if ('0' <= ch && ch <= '9') {
                arr.add(ch-'0');
            }
        }
        Collections.sort(arr);
        return arr.stream()
                .mapToInt(i -> i)
                .toArray();
    }
}