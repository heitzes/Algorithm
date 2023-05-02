import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) return new int[] {-1};
        int[] answer = new int[arr.length-1];
        int[] copy = Arrays.copyOf(arr, arr.length);
        Arrays.sort(copy);
        String str = "";
        int mini = copy[0];
        for (int i=0;i<arr.length;i++) {
            if (arr[i] != copy[0]) {
                str += arr[i] + " ";
            }
        }
        str = str.trim();
        String[] spt = str.split(" ");
        for (int i=0;i<answer.length;i++) {
            answer[i] = Integer.parseInt(spt[i]);
        }
        return answer;
    }
}