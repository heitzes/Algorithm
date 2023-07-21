import java.util.*;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap();
        map.put(a, map.getOrDefault(a, 0)+1);
        map.put(b, map.getOrDefault(b, 0)+1);
        map.put(c, map.getOrDefault(c, 0)+1);
        map.put(d, map.getOrDefault(d, 0)+1);
        int size = map.size();
        Set<Map.Entry<Integer, Integer>> entry = map.entrySet();
        Iterator it = entry.iterator();
        Map.Entry<Integer, Integer> o1 = null, o2 = null, o3 = null;
        Integer p = 0, q = 0, r = 0;
        switch(size) {
            case 1:
                answer += 1111 * a;
                break;
            case 2:
                o1 = (Map.Entry<Integer, Integer>)it.next();
                o2 = (Map.Entry<Integer, Integer>)it.next();
                p = o1.getKey();
                q = o2.getKey();
                if (o1.getValue() == 2) {
                    answer += (p + q) * Math.abs(p-q);
                } else {
                    answer += o1.getValue() == 3 ? Math.pow(10*p + q,2) : Math.pow(10*q + p,2);
                }
                break;
            case 3:
                o1 = (Map.Entry<Integer, Integer>)it.next();
                o2 = (Map.Entry<Integer, Integer>)it.next();
                o3 = (Map.Entry<Integer, Integer>)it.next();
                p = o1.getKey();
                q = o2.getKey();
                r = o3.getKey();
                if (o1.getValue() == 2) {
                    answer += q * r;
                } else if (o2.getValue() == 2) {
                    answer += p * r;
                } else {
                    answer += p * q;
                }
                break;
            case 4:
                answer += Math.min(Math.min(a, b), Math.min(c, d));
                break;
        }
        
        
        return answer;
    }
}