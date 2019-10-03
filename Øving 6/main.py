def generate_list_by_file(filename):
    strings = []  # Creates a empty list which will be filled with the different words
    with open(filename, 'r') as f:
        for line in f:
            strings.append(line.rstrip())  # Adds the different words from the filename

    return strings


# Method to swap two indexes in a given array
def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


def bubble_sort(alist):  # Standard bubblesort
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            # If the length of te words is greather than the next we want those to switch places
            if len(alist[i]) > len(alist[i + 1]):
                swap(alist, i, (i + 1))
            #If the length is the same we want to sort by the alphabet
            elif len(alist[i]) == len(alist[i + 1]):
                if alist[i] > alist[i + 1]:
                    swap(alist, i, (i + 1))
