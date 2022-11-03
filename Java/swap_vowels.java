import java.util.Arrays;

/**
 * swap_vowels
 */
public class swap_vowels {
    public Boolean isVowels(char c) {
        if ("aeiou".contains(String.valueOf(c))) {
            return true;
        }
        return false;
    }
    public String reverseVowels(String s) {
        int right_ind = s.length() - 1;
        int left_ind = 0;

       char[] x = s.toCharArray();

        while (right_ind >= left_ind) {
            // swap if both are vowels
            if (isVowels(x[left_ind]) && isVowels(x[right_ind])) {
                char temp = x[left_ind];
                x[left_ind] = x[right_ind];
                x[right_ind] = temp;
                left_ind += 1;
                right_ind -= 1;
                continue;
            }
            if (isVowels(x[left_ind]) && !isVowels(x[right_ind])) {
                right_ind -= 1;
                continue;
            }

            if (!isVowels(x[left_ind]) && isVowels(x[right_ind])) {
                left_ind += 1;
                continue;
            }
            
            left_ind += 1;
            right_ind -= 1;
            
        }
        
        return new String(x);
    }

    public static void main(String[] args) {
        swap_vowels obj = new swap_vowels();
        System.out.println(obj.reverseVowels("hello"));
    }
}