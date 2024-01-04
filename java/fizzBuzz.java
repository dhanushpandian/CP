import java.util.*;

public class Fizzbuzz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // int n = 10;
        String[] a = new String[n];
        int i = 1; // Start from index 0
        while (i < n+1) {

            if (i    % 3 == 0 && i % 5 == 0) {
                a[i-1 ] = "FizzBuzz"; // Adjust the index for zero-based indexing
            } else if (i % 3 == 0) {
                a[i -1] = "Fizz";
            } else if (i % 5 == 0) {
                a[i -1] = "Buzz";
            } else {
                a[i-1 ] = String.valueOf(i);
            }
            i++; // Increment i to avoid an infinite loop
        }
        for (String s : a) {
            System.out.print(s + " "); // Add a space for better output formatting
        }
    }
}
