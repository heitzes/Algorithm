class Solution {
    public int solution(int[] numbers) {
        int ref = 45;
        for (int num: numbers) {
            ref -= num;
        }
        return ref;
    }
}