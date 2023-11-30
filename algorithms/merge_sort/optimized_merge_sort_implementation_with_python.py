# Python program for implementation of MergeSort

def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L (if any)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R (if any)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver Code
if __name__ == '__main__':
    # Allowing the code to accept input from users
    arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]

    print("Given array is:")
    printList(arr)

    mergeSort(arr)

    print("\nSorted array is:")
    printList(arr)

