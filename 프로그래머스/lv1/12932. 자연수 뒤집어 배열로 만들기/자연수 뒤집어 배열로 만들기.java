class Solution {
    public int[] solution(long n) {
        String str = "" + n;
        int[] answer = new int[str.length()];
        for(int i=0; i<str.length(); i++){
            int num = (int) (n % 10);
            answer[i] = num;
            n /= 10;
        }
        return answer;
    }
}