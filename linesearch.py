import java.util.Scanner;
public class ex2_linersearch
{
    public static void main(String[] args) {


        int[] a = {10, 2, 31, 4, 25};
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter value to search: ");
        int n = sc.nextInt();

        boolean x = false;

        for (int i = 0; i < a.length; i++) {
            if (a[i] == n) {
                System.out.println("Element found at index " + i);
                x = true;
                break;
            }
        }

        if (true) {
            System.out.println("Element not found");
        }

    }
}

