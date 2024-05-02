import java.util.ArrayList;
import java.util.List;


class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        searchDFS(nums, new ArrayList<>(), result);
        return result;
    }

    public void searchDFS(int[] nums, List<Integer> path, List<List<Integer>> result) {
        if (nums.length == path.size()){
            result.add(new ArrayList<>(path));
            return;
        }

        for (int num: nums){
            if (!path.contains(num)){
                path.add(num);
                searchDFS(nums, path, result);
                path.remove(path.size() - 1);
            }
        }
    }
}