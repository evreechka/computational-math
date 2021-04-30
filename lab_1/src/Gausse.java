import java.util.Arrays;

public class Gausse {

    public Matrix methodGausse(Matrix matrix) {
        Matrix copyMatrix = new Matrix(matrix.getRowsSize(), matrix.getColumnsSize());
        for (int i = 0; i < matrix.getRowsSize(); i++) {
            for (int j = 0; j < matrix.getColumnsSize(); j++) {
                copyMatrix.setElement(i, j, matrix.getElement(i, j));
            }
        }
        for (int k = 0; k < copyMatrix.getRowsSize() - 1; k++) {
            if (copyMatrix.getElement(k, k) == 0) continue;
            for (int i = k + 1; i < copyMatrix.getRowsSize(); i++) {
                if (copyMatrix.getElement(i, k) == 0) continue;
                double specialEl = copyMatrix.getElement(i, k);
                for (int j = 0; j < copyMatrix.getColumnsSize(); j++) {
                    copyMatrix.getMatrix()[i][j] -= (double) Math.round(copyMatrix.getElement(k, j) * (specialEl / copyMatrix.getElement(k, k)) * 100) / 100;
                }
            }
        }
        return copyMatrix;
    }
    public double getDeterminate(Matrix matrix) {
        Matrix triangleMatrix = methodGausse(matrix);
        double determinate = 1;
        for (int i = 0; i < triangleMatrix.getRowsSize(); i++) {
            determinate *= triangleMatrix.getElement(i, i);
        }
        if (determinate == 0) determinate = Math.abs(determinate);
        return determinate;
    }

    public double[] getUnknownColumns(Matrix matrix) {
        Matrix triangle = methodGausse(matrix);
        if (isInjoint(triangle)) return null;
        double[] unknowns = getNullColumn(triangle.getRowsSize());
        for (int i = triangle.getRowsSize() - 1; i >= 0; i--) {
            double elementsSum = 0;
            double b = triangle.getElement(i, triangle.getColumnsSize() - 1);
            if (!isNullRow(triangle.getRow(i)) && triangle.getElement(i, i) != 0) {
                for (int j = 0; j < triangle.getColumnsSize() - 1; j++) {
                    if (j != i) elementsSum += unknowns[j] * triangle.getElement(i, j);
                }
                unknowns[i] = (b - elementsSum) / triangle.getElement(i, i);
            }
        }
        return unknowns;
    }

    public double[] getResidualColumns(Matrix matrix) {
        Matrix triangle = methodGausse(matrix);
        if (isInjoint(triangle)) return null;
        double[] unknowns = getUnknownColumns(matrix);
        double[] residuals = new double[unknowns.length];
        for (int i = triangle.getRowsSize() - 1; i >= 0; i--) {
            double b = triangle.getElement(i, triangle.getColumnsSize() - 1);
            double elementsSum = 0;
            for (int j = 0; j < triangle.getColumnsSize() - 1; j++) {
                elementsSum += unknowns[j] * triangle.getElement(i, j);
            }
            residuals[i] = b - elementsSum;
        }
        return residuals;
    }

    private double[] getNullColumn(int size) {
        double[] column = new double[size];
        for (int i = 0; i < size; i++) {
            column[i] = 0;
        }
        return column;
    }

    private boolean isNullRow(double[] row) {
        for (int i = 0; i < row.length - 1; i++) {
            if (row[i] != 0) return false;
        }
        return true;
    }

    private boolean isInjoint(Matrix matrix) {
        for (int i = 0; i < matrix.getRowsSize(); i++) {
            if (isNullRow(matrix.getRow(i)) && matrix.getElement(i, matrix.getColumnsSize() - 1) != 0) return true;
        }
        return false;
    }
}
