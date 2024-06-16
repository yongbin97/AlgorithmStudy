class Solution {
    public boolean isPalindrome(String s) {
        String afterString = removeAllNonAlphaNumeric(s);

        int halfOfStringLength = afterString.length() / 2;

        for (int i = 0; i < halfOfStringLength; i ++){
            if (afterString.charAt(i) != afterString.charAt(afterString.length() - i - 1)){
                return false;
            }
        }
        return true;
    }

    private String removeAllNonAlphaNumeric(String s){
        if (s == null){
            return "";
        } else {
            return s.toUpperCase().replaceAll("[^A-Za-z0-9]", "");
        }
    }
}