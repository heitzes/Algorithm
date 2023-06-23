class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[2];
        int maxw = board[0]/2, maxh = board[1]/2;
        int left = 0, right = 0, up = 0, down = 0;
        for (String inp : keyinput) {
            if (inp.equals("left")) {
                if (Math.abs(answer[0] - 1) <= maxw) answer[0] -= 1;
            } else if(inp.equals("right")) {
                if (Math.abs(answer[0] + 1) <= maxw) answer[0] += 1;
            } else if(inp.equals("up")) {
                if (Math.abs(answer[1] + 1) <= maxh) answer[1] += 1;
            } else {
                if (Math.abs(answer[1] - 1) <= maxh) answer[1] -= 1;
            }
        }        
        return answer;
    }
}