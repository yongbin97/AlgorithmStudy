import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(n, k, new ArrayList<>(), result);
        return result;
    }

    public void dfs(int n, int k, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == k) {
            result.add(new ArrayList<>(path));
            return;
        }

        int start = 1;
        if (path.size() > 0) start = path.get(path.size() - 1) + 1;
        int last = n - k + path.size() + 2;

        for (int i = start; i < last; i++) {
            path.add(i);
            dfs(n, k, path, result);
            path.remove(path.size() - 1);
        }
    }
}