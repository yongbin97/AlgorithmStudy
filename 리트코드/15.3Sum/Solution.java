import java.util.*;


class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int[] sortedNums = Arrays.stream(nums).sorted().toArray();
        Set<List<Integer>> result = new HashSet<>();

        for (int i = 0; i < sortedNums.length - 2; i++){
            int left = i + 1;
            int right = sortedNums.length - 1;

            while (left < right) {
                if (sortedNums[left] + sortedNums[right] + sortedNums[i] == 0){
                    result.add(Arrays.asList(sortedNums[i], sortedNums[left], sortedNums[right]));
                    left ++;
                    right --;
                } else if (sortedNums[left] + sortedNums[right] + sortedNums[i] > 0){
                    right --;
                } else {
                    left ++;
                }
            }
        }
        return new ArrayList<>(result);
    }
}