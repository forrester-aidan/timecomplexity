import time  # Imports the time module into the file
import stringdata  # Imports the stringdata module into the file


def linear_search(container: tuple[str], element: str):  # Searches through the container one by one
    index = 0

    while index < len(container):
        if container[index] == element:
            return index
        else:
            index += 1

    return -1


def binary_search(container: tuple[str], element: str):  # Searches through the container by half slices
    beginning = 0
    end = len(container) - 1

    while beginning <= end:
        mid = int(beginning + (end - beginning) / 2)

        if container[mid] == element:
            return mid
        elif container[mid] > element:
            end = mid - 1
        else:
            beginning = mid + 1

    return -1


def main():  # Begins the program
    dataset = stringdata.get_data()
    counter = 0

    while counter < 6:  # Loops through the if statement 6 times
        beginningTime = time.time()
        if counter == 0:  # Each if statement checks either linear search or binary search
            print("not_here linear index: " + str(linear_search(dataset, "not_here")))
            endTime = time.time()
            elapsed = endTime - beginningTime
            print("not_here linear search time: " + str(elapsed))
            counter += 1
        elif counter == 1:
            print("not_here binary index: " + str(binary_search(dataset, "not_here")))
            endTime = time.time()
            elapsed = endTime - beginningTime
            print("not_here binary search time: " + str(elapsed) + "\n")
            counter += 1
        elif counter == 2:
            print("mzzzz index: " + str(linear_search(dataset, "mzzzz")))
            endTime = time.time()
            elapsed = endTime - beginningTime
            print("mzzzz linear search time: " + str(elapsed))
            counter += 1
        elif counter == 3:
            print("mzzzz binary index: " + str(binary_search(dataset, "mzzzz")))
            endTime = time.time()
            elapsed = endTime - beginningTime
            print("mzzzz binary search time: " + str(elapsed) + "\n")
            counter += 1
        elif counter == 4:
            print("aaaaa index: " + str(linear_search(dataset, "aaaaa")))
            endTime = time.time()
            elapsed = endTime - beginningTime
            print("aaaaa linear search time: " + str(elapsed))
            counter += 1
        elif counter == 5:
            print("aaaaa binary index: " + str(binary_search(dataset, "aaaaa")))
            endTime = time.time()
            elapsed = endTime - beginningTime
            print("aaaaa binary search time: " + str(elapsed))
            counter += 1


if __name__ == '__main__':  # Runs the program
    main()
