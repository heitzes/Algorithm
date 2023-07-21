class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        int r = box[0], c = box[1], h = box[2];
        answer = (r/n) * (c/n) * (h/n);
        return answer;
    }
}