class Solution {
    public int[][] merge(int[][] intervals) {
        List<List<Integer>> resList = new ArrayList<>();
		
		Arrays.sort(intervals, (o1, o2) -> {
			if (o1[0] == o2[0]) return o1[1] - o2[1];
			else return o1[0] - o2[0];
		});
		
		int left = intervals[0][0];
		int right = intervals[0][1];
		
		for (int i = 1; i < intervals.length; i++) {
			int[] curr = intervals[i];
			
			if (curr[0] > right) {
				resList.add(Arrays.asList(left, right));
				
				left = curr[0];
				right = curr[1];
			} else {
				right = curr[1];
			}
			
		}
        resList.add(Arrays.asList(left, right));

		
		int[][] res = new int[resList.size()][2];
		
		for (int i = 0; i < resList.size(); i++) {
			res[i][0] = resList.get(i).get(0);
			res[i][1] = resList.get(i).get(1);
		}
		
		return res;
    }
}