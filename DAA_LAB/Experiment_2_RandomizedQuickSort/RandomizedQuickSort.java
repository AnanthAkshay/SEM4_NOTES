import java.util.Random;

public class RandomizedQuickSort {

    static Random rand = new Random();

    public static void quickSort(int arr[], int low, int high) {
        if (low < high) {

            int pivotIndex = randomPartition(arr, low, high);

            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    public static int randomPartition(int arr[], int low, int high) {

        int randomIndex = low + rand.nextInt(high - low + 1);

        swap(arr, randomIndex, high);

        return partition(arr, low, high);
    }

    public static int partition(int arr[], int low, int high) {

        int pivot = arr[high];

        int i = low - 1;

        for (int j = low; j < high; j++) {

            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);

        return i + 1;
    }

    public static void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {

        int n = 1000; // Number of packages

        int packages[] = new int[n];

        for (int i = 0; i < n; i++) {
            packages[i] = rand.nextInt(10000);
        }

        System.out.println("First 20 Package IDs Before Sorting:");
        for (int i = 0; i < 20; i++) {
            System.out.print(packages[i] + " ");
        }

        long startTime = System.nanoTime();

        quickSort(packages, 0, n - 1);

        long endTime = System.nanoTime();

        System.out.println("\n\nFirst 20 Package IDs After Sorting:");
        for (int i = 0; i < 20; i++) {
            System.out.print(packages[i] + " ");
        }

        System.out.println("\n\nExecution Time: "
                + (endTime - startTime) + " nanoseconds");
    }
}
