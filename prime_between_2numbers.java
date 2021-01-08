public class prime_between_2numbers {
    public Boolean isPrime(int x) {
        for (int i = 2; i < x; i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    public void qn1(int x, int y) {
        for (int i = x; i < y; i++) {
            if (isPrime(i)) {
                System.out.println(i + " ");
            }
        }
    }

    public static void main(String[] args) {
        prime_between_2numbers obj = new prime_between_2numbers();
        obj.qn1(30, 70);
    }
}
