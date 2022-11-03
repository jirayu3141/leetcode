public class reverse_integer {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && pop > 7))
                return 0;
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && pop < -8))
                return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }

    public static void main(String[] args) {
        reverse_integer obj = new reverse_integer();
        System.out.println("reversing -123....we get: " + obj.reverse(-123));
        System.out.println("reversing 123....we get: " + obj.reverse(123));
        System.out.println("reversing 120....we get: " + obj.reverse(120));
        System.out.println("reversing 0....we get: " + obj.reverse(0));
        System.out.println("reversing 1534236469....we get: " + obj.reverse(1534236469));
        System.out.println("reversing 1463847412....we get: " + obj.reverse(1463847412));
        System.out.println("reversing 1563847412....we get: " + obj.reverse(1563847412));

    }
}
