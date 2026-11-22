def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))

    insertion_sort(numbers)

    for x in numbers:
        print(x)


if __name__ == "__main__":
    main()