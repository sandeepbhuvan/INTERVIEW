import java.util.Arrays;

public class BinarySort {
    public static void binarySort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int key = array[i];
            int left = 0;
            int right = i - 1;

            // Find the position to insert the element using binary search
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (array[mid] > key) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            // Shift elements to make space for the key
            for (int j = i - 1; j >= left; j--) {
                array[j + 1] = array[j];
            }
            array[left] = key;
        }
    }

    public static void main(String[] args) {
        int[] array = {5, 3, 8, 4, 2, 7, 1, 10, 6, 9};
        System.out.println("Original array: " + Arrays.toString(array));
        binarySort(array);
        System.out.println("Sorted array: " + Arrays.toString(array));
    }
}
