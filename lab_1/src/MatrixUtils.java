import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class MatrixUtils {
    private Scanner scanner = new Scanner(System.in);
    public Matrix createMatrix() throws IOException {
        int inputWay;
        while (true) {
            System.out.println("Как вы хотите ввести матрицу (1 - с помощью файла; 2 - вручную; 3 - случайные коэффициенты):");
            inputWay = scanner.nextInt();
            if (inputWay != 1 && inputWay != 2 && inputWay != 3) {
                System.out.println("Выберете способ из предложенных!");
            } else {
                break;
            }
        }
        Matrix matrix;
        switch (inputWay) {
            case (1): {
                matrix = readFromFile();
                break;
            }
            case (2): {
                int rowSize = getRowsSize();
                matrix = readFromConsole(rowSize, rowSize + 1);
                break;
            }
            case (3): {
                int rowSize = getRowsSize();
                matrix = generateMatrix(rowSize, rowSize + 1);
                break;
            }
            default:
                throw new IllegalStateException("Unexpected value: " + inputWay);
        }
        return matrix;
    }

    private int getRowsSize() {
        while (true) {
            System.out.println("Введите количество строк матрицы:");
            int rowsSize = scanner.nextInt();
            if (rowsSize > 20) {
                System.out.println("Количество строк не может превышать 20!");
            } else {
                return rowsSize;
            }
        }
    }

    private Matrix readFromConsole(int rowsSize, int columnsSize) {
        System.out.println("Введите матрицу:");
        return new Matrix(rowsSize, columnsSize, readMatrix(scanner, rowsSize, columnsSize));
    }

    private Matrix readFromFile() throws IOException {
        File file;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Введите имя файла:");
            String filename = "resources/" + scanner.nextLine();
            file = new File(filename);
            if (!file.exists()) {
                System.out.println("Такого файла не существует :(");
            } else {
                break;
            }
        }
        Scanner matrixReader = new Scanner(file);
        int rowsSize = matrixReader.nextInt();
        return new Matrix(rowsSize, rowsSize + 1, readMatrix(matrixReader, rowsSize, rowsSize + 1));
    }

    private Matrix generateMatrix(int rowsSize, int columnsSize) {
        double[][] matrix = new double[rowsSize][columnsSize];
        for (int i = 0; i < rowsSize; i++) {
            for (int j = 0; j < columnsSize; j++) {
                matrix[i][j] = (double) Math.round((Math.random() * 10) * 100) / 100;
            }
        }
        return new Matrix(rowsSize, rowsSize + 1, matrix);
    }

    public void printMatrix(Matrix matrix) {
        for (int i = 0; i < matrix.getRowsSize(); i++) {
            for (int j = 0; j < matrix.getColumnsSize(); j++) {
                if (j == matrix.getColumnsSize() - 1) {
                    System.out.printf("| %.2f", matrix.getElement(i, j));
                } else {
                    System.out.printf("%.2f ", matrix.getElement(i, j));
                }

            }
            System.out.println();
        }
    }


    public void printColumn(double[] column) {
        for (double v : column) {
            System.out.println(v);
        }
    }

    private double[][] readMatrix(Scanner input, int rowsSize, int columnsSize) {
        double[][] matrix = new double[rowsSize][columnsSize];
        for (int i = 0; i < rowsSize; i++) {
            for (int j = 0; j < columnsSize; j++) {
                matrix[i][j] = input.nextDouble();
            }
        }
        return matrix;
    }
}
