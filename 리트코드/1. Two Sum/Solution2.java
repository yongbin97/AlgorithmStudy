import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[][] numsIdxList = new int[nums.length][2];

        for (int i = 0; i < nums.length; i++){
            numsIdxList[i][0] = nums[i];
            numsIdxList[i][1] = i;
        }
        Arrays.sort(numsIdxList, Comparator.comparing(x -> x[0]));

        int left = 0;
        int right = numsIdxList.length - 1;

        while (left < right){
            if (numsIdxList[left][0] + numsIdxList[right][0] == target){
                left = numsIdxList[left][1];
                right = numsIdxList[right][1];
                break;
            } else if (numsIdxList[left][0] + numsIdxList[right][0] >= target){
                right --;
            } else {
                left ++;
            }
        }

        return new int[] {left, right};
    }
}