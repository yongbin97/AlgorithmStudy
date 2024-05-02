import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> numsList = Arrays.stream(nums).boxed().collect(Collectors.toList());
        searchDFS(numsList, new ArrayList<>(), result);
        return result;
    }

    public void searchDFS(List<Integer> nums, List<Integer> path, List<List<Integer>> result) {
        if (nums.size() == 0) {
            result.add(path);
            return;
        }

        for (int num : nums) {
            List<Integer> newNums = nums.stream().filter(ele -> ele != num).collect(Collectors.toList());
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(num);
            searchDFS(newNums, newPath, result);
        }
    }
}