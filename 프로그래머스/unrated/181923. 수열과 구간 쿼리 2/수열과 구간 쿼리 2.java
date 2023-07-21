class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int q=0; q<queries.length; q++) {
            int[] query = queries[q];
            int val = -1;
            for (int i=query[0]; i<=query[1]; i++) {
                if (arr[i] > query[2]) {
                    val = val == -1 ? arr[i] : Math.min(val, arr[i]);
                }
            }
            answer[q] = val;
        }
        return answer;
    }
}