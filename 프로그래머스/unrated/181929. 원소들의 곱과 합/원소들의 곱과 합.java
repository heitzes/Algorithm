class Solution {
    public int solution(int[] num_list) {
        int multi = 1;
        int pow = 0;
        for (int num : num_list) {
            multi *= num;
            pow += num;
        }
        return multi < pow*pow ? 1:0;
    }
}