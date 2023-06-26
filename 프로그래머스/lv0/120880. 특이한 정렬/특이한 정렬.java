import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        Integer[] arr = Arrays.stream(numlist).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, new Comparator<Integer>() {
            public int compare(Integer o1, Integer o2) {
                Integer abs1 = Math.abs(o1-n);
                Integer abs2 = Math.abs(o2-n);
                if (abs1.equals(abs2)) {
                    return o2-o1;
                } else if(abs1<abs2) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });
        return Arrays.stream(arr).mapToInt(i->i).toArray();
    }
}