public class ex2_binary_search
{
    public static void main(String[] args) {
        int[] a = {10, 20, 30, 40, 50};
        int x = 30;

        int low = 0;
        int high = a.length - 1;
        int mid;

        while (low <= high)
        {
            mid = (low + high) / 2;

            if (a[mid] == x)
            {
                System.out.println("Element found at index " + mid);
                return;
            }
            else if (a[mid] < x)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }

        System.out.println("Element not found");
    }
}
