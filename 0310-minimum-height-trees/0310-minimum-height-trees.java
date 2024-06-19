class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return List.of(0);

        // 1. set edges Maps {Node: List<Node>}
        Map<Integer, List<Integer>> edgeMap = new HashMap<>();
        for (int[] nodes : edges) {
            edgeMap.putIfAbsent(nodes[0], new ArrayList<>());
            edgeMap.putIfAbsent(nodes[1], new ArrayList<>());

            edgeMap.get(nodes[0]).add(nodes[1]);
            edgeMap.get(nodes[1]).add(nodes[0]);
        }

        // 2. set initial leaves nodes
        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (edgeMap.get(i).size() == 1)
                leaves.add(i);
        }

        // 3. remove leaves until n < 2
        while (n > 2) {
            n -= leaves.size();

            List<Integer> newLeaves = new ArrayList<>();
            for (int leaf : leaves){
                // leaf는 하나의 neighbor만 가진다.
                int neighbor = edgeMap.get(leaf).get(0);

                edgeMap.get(neighbor).remove((Object) leaf);
                if (edgeMap.get(neighbor).size() == 1) newLeaves.add(neighbor);
            }

            leaves = newLeaves;
        }

        return leaves;
    }
}