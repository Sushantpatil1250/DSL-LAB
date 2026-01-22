public class ex2_matrix_sub {
    public static void main(String[] args) {


        int[][] a = {{2, 5, 6,}, {5, 9, 3}};
        int[][] b = {{2, 5, 6,}, {5, 9, 3}};
        int[][] c = {{0, 0, 0}, {0, 0, 0,}};
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                c[i][j] = a[i][j] * b[i][j];
            }
        }
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < c[i].length; j++) {
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
    }
}
