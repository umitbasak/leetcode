class Solution {
    int getSum(int a, int b) {
        int carry = (a & b) << 1;
        int xor = a ^ b;

        if (carry == 0) {
            return xor;
        }

        return getSum(carry, xor);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.getSum(-1, 1);
    }
}
