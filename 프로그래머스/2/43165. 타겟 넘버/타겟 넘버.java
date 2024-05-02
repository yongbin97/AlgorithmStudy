class Solution {
    public int solution(int[] numbers, int target) {
        int currSum = 0;
        return search(1, currSum + numbers[0], numbers, target) + search(1, currSum - numbers[0], numbers, target);
    }
    
    public int search(int idx, int currSum, int[] numbers, int target){
        if (idx == numbers.length){
            if (currSum == target) return 1;
            else return 0;
        }
        return search(idx + 1, currSum + numbers[idx], numbers, target) + search(idx + 1, currSum - numbers[idx], numbers, target);       
    }
}