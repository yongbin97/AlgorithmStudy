class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int leftMax = height[left];
        int rightMax = height[right];
        int volume = 0;

        while (left < right){
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);

            if (leftMax <= rightMax){
                volume += leftMax - height[left];
                left ++;
            } else {
                volume += rightMax - height[right];
                right --;
            }
        }

        return volume;
    }
}