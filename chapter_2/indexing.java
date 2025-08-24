package chapter_2;

public class indexing {
    public static void main(String[] args) {
        int[][] matrix = {
            {1,2,3,4,5},
            {6,7,8,9,10},
            {11,12,13,14,15},
            {16,17,18,19,20},
            {21,22,23,24,25}
        };
        System.out.println(get_adj_cell_sum(matrix, 0, 0));
    }

    public static int get_adj_cell_sum(int[][] matrix, int cx, int cy) {
        int sum = -matrix[cx][cy];
        for (int i = cx-1; i <= cx+1; i++) {
            for (int j = cy-1; j <= cy+1; j++) {
                try {
                    sum += matrix[i][j];
                } catch (Exception e) {
                    // pass
                }
            }
        }
        return sum;
    }
}
