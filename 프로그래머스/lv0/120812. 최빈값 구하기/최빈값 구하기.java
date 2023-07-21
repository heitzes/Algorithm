import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] count = new int[1000];
        for (int i=0; i < array.length; i++) {
            count[array[i]] += 1;
        }
        int[] ref = new int[1000];
        System.arraycopy(count, 0, ref, 0, 1000);
        Arrays.sort(ref);
        int maximum = ref[999];
        boolean find = false;
        
        for (int i=0; i < 1000; i++) {
            if (!find && (count[i] == maximum)) {
                find = true;
                answer = i;
                continue;
            }
            if (find && (count[i] == maximum)) {
                answer = -1;
                break;
            }
        }
        return answer;
    }
}