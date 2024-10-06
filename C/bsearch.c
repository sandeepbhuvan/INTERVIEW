#include <stdio.h>

int binarySearch(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Check if target is present at mid
        if (arr[mid] == target)
            return mid;

        // If target greater, ignore left half
        if (arr[mid] < target)
            left = mid + 1;

        // If target is smaller, ignore right half
        else
            right = mid - 1;
    }

    // Target is not present in array
    return -1;
}

int main() {
    printf("Enter the number of elements: ");
    int n;
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements: ");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("Enter the target element: ");
    int target;
    scanf("%d",&target);
    int result = binarySearch(arr, n, target);
    if (result != -1)
        printf("Element is present at index %d\n", result);
    else
        printf("Element is not present in array\n");
    return 0;
}