public class Matrix {
    private int rowsSize;
    private int columnsSize;
    private double[][] matrix;

    public Matrix(int rowsSize, int columnsSize) {
        this.rowsSize = rowsSize;
        this.columnsSize = columnsSize;
        matrix = new double[rowsSize][columnsSize];
    }

    public Matrix(int rowsSize, int columnsSize, double[][] matrix) {
        this.rowsSize = rowsSize;
        this.columnsSize = columnsSize;
        this.matrix = matrix;
    }

    public int getColumnsSize() {
        return columnsSize;
    }

    public int getRowsSize() {
        return rowsSize;
    }

    public double[][] getMatrix() {
        return matrix;
    }

    public void setColumnsSize(int columnsSize) {
        this.columnsSize = columnsSize;
    }

    public void setRowsSize(int rowsSize) {
        this.rowsSize = rowsSize;
    }

    public void setMatrix(double[][] matrix) {
        this.matrix = matrix;
    }

    public void setElement(int i, int j, double value) {
        this.matrix[i][j] = value;
    }

    public double getElement(int i, int j) {
        return matrix[i][j];
    }

    public void setRow(int i, double[] row) {
        matrix[i] = row;
    }

    public double[] getRow(int i) {
        return matrix[i];
    }

}
