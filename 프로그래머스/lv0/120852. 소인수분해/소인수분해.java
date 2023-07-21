import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=2; i<=n; i++) {
            if (n % i == 0) {
                boolean flag = true;
                for (int other : arr) {
                    if (i % other == 0) {
                        flag = false;
                    }
                }
                if (flag) arr.add(i);
            }
        }
        return arr.stream().mapToInt(i->i).toArray();
    }
}