class Solution {
    public String solution(String phone_number) {
        int length = phone_number.length();
        String sub = phone_number.substring(length-4);
        String stars = phone_number.replaceAll("[0-9]", "*");
        return stars.substring(0, length-4) + sub;
    }
}