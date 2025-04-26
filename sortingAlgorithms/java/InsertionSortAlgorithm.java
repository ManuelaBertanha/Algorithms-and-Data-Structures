package sortingAlgorithms.java;

public class InsertionSortAlgorithm {
    
    public static void insertionSort(int[] sequence, int n) {

        int key, j;
        for (int i = 1; i < n; i++) {
            key = sequence[i];
            j = i - 1;

            while (j >= 0 && sequence[j] > key) {
                sequence[j + 1] = sequence[j];
                j--;
            }
            sequence[j + 1] = key;
        }
    }    
    
    public static void main(String[] args) {

        int[] sequence = { 7, 2, 9, 1, 5, 0, 8, 4, 6, 3, 9, 0, 11, 125, 13, 2, 500 };
        insertionSort(sequence, sequence.length);
        for (int num : sequence) System.out.print(num + " ");
    }
    
}