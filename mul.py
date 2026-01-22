public class ex2_matrix_multiplication
{
    public static void main(String[] args) {

        int [][] a = {{2,5,6},{5,9,3}};
        int [][] b = {{2,5},{6,5},{9,3}};
        int [][] c = new int[2][2];

        for (int i = 0; i < a.length; i++)
        {
            for (int j = 0; j < b[0].length; j++)
            {
                c[i][j] = 0;
                for (int k = 0; k < a[0].length; k++)
                {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        for (int i = 0; i < c.length; i++)
        {
            for (int j = 0; j < c[i].length; j++)
            {
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
    }
}
