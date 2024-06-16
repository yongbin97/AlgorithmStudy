import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> candidatesList = Arrays.stream(candidates).boxed().collect(Collectors.toList());
        dfs(candidatesList, target, 0, new LinkedList<>(), result);
        return result;
    }

    public void dfs(List<Integer> candidates, int target, int sum, LinkedList<Integer> curr, List<List<Integer>> result) {
        if (sum == target) {
            result.add(new ArrayList<>(curr));
            return;
        } else if (sum > target) return;

        for (int i = 0; i < candidates.size(); i++) {
            curr.add(candidates.get(i));
            dfs(candidates.subList(i, candidates.size()), target, sum + candidates.get(i), curr, result);
            curr.removeLast();
        }
    }
}