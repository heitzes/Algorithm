class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        StringBuilder even = new StringBuilder();
        StringBuilder odd = new StringBuilder();
        for (int i : num_list) {
            if (i%2==0) even.append(i);
            else odd.append(i);
        }
        answer = Integer.parseInt(even.toString()) + Integer.parseInt(odd.toString());
        return answer;
    }
}