class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        StringBuilder sb = new StringBuilder(my_string);
        for (int[] q : queries) {
            StringBuilder rev = new StringBuilder(sb.substring(q[0], q[1]+1));
            sb.replace(q[0], q[1]+1, rev.reverse().toString());
        }
        return sb.toString();
    }
}