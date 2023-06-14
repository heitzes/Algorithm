import java.util.*;
class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] answer = new int[numbers.length];
        int lastIndex = numbers.length-1;
        if (direction.equals("right")) {
            answer[0] = numbers[lastIndex];
            System.arraycopy(numbers, 0, answer, 1, lastIndex);
        } else {
            System.arraycopy(numbers, 1, answer, 0, lastIndex);
            answer[lastIndex] = numbers[0];
        }
        
        return answer;
    }
}