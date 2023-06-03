class Solution {
    public String solution(String my_string, int n) {
        StringBuffer sb = new StringBuffer();
        for (char ch : my_string.toCharArray()) {
            sb.append((""+ch).repeat(n));
        }
        return sb.toString();
    }
}