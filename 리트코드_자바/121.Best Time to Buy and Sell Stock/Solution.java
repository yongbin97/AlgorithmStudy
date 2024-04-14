class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = 10000;
        int maxProfit = 0;

        for (int price: prices){
            if (minPrice > price){
                minPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }
        return maxProfit;
    }
}