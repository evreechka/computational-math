import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        MatrixUtils worker = new MatrixUtils();
        Gausse gausse = new Gausse();
        Matrix matrix = worker.createMatrix();
        System.out.println("Введенная расширенная матрица:");
        worker.printMatrix(matrix);
        System.out.println("Определитель данной матрицы:");
        System.out.printf("%.2f%n", gausse.getDeterminate(matrix));
        Matrix triangle = gausse.methodGausse(matrix);
        System.out.println("Матрица после приведения к треугольному виду:");
        worker.printMatrix(triangle);
        double[] unknowns = gausse.getUnknownColumns(matrix);
        System.out.println("Столбец неизвестных:");
        if (unknowns == null) {
            System.out.println("Матрица несвоместна");
        } else {
            worker.printColumn(unknowns);
        }
        double[] residuals = gausse.getResidualColumns(matrix);
        System.out.println("Столбец невязок:");
        if (residuals == null) {
            System.out.println("Матрица несовместна");
        } else {
            worker.printColumn(residuals);
        }
    }
}
