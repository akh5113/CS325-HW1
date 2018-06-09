# Anne Harris
# CS 325-400
# Homework 1

import math

# MERGE SORT
# Implementation based off of "Introduction to Algorithms by Corment, Leiserson, Erivest, Stein, 3rd ed.
# Page 31
# Implementation also based off of this site: https://www.geeksforgeeks.org/merge-sort/
# merge function
def merge(array, first, middle, last):
    # find length of the sub arrays
    n1 = middle - first + 1
    n2 = last - middle

    # create sub arrays
    L = [0]*n1
    R = [0]*n2

    # fill the Left and Right arrays
    L = array[first:middle+1]
    R = array[middle + 1:]

    # set indexes to zero
    i = 0
    j = 0
    # set k to equal the start
    k = first

    # merge arrays back together
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # the remaining elements in the array, if needed
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


# merge sort
def mergesort(array, left, right):
    if left < right:
        median = math.floor((left + right)/2)
        # sort first half
        mergesort(array, left, median)
        # sort second half
        mergesort(array, median+1, right)
        # merge
        merge(array, left, median, right)


# IMPORT FILE
# File I/O based of off implementation discussed on Slack
nums = []
with open("data.txt", "r") as f:
    for x in f:
        var = x.split(" ")
        for y in range(len(var)):
            var[y] = int(var[y])    # string into integer
        nums.append(var[1:])        # we don't want first number as it's the count of the line

f.close()

# test cases
# test = [15, 19, 3, 11, 9, 7, 17]
# size = len(test)

print("Merge Sort")
# print from file
arraySize = len(nums)
# print the unsorted arrays
print("The unsorted arrays are: ")
for a in range(arraySize):
    print(nums[a])

# sort the arrays
for listM in nums:
    mergesort(listM, 0, (len(listM)-1))

print("The sorted arrays are: ")
for b in range(arraySize):
    print(nums[b])

# store sorted array in .txt output
fOut = open("merge.out", "w+")
for nLine in range(arraySize):
    number = nums[nLine]
    for x in range(len(number)):
        fOut.write(str(number[x]))
        fOut.write(" ")
    fOut.write("\n")
fOut.close()


# INSERT SORT
# Implementation based off of "Introduction to Algorithms by Corment, Leiserson, Erivest, Stein, 3rd ed.
# Page 18
def insertsort(arrayIn):
    j = 2
    for j in range(len(arrayIn)):
        key = arrayIn[j]
        # insert key into sorted sequence
        i = j - 1
        while i >= 0 and arrayIn[i] > key:
            arrayIn[i + 1] = arrayIn[i]
            i -= 1
        arrayIn[i + 1] = key

# IMPORT FILE
nums2 = []
with open("data.txt", "r") as f:
    for x in f:
        item = x.split(" ")
        for y in range(len(item)):
            item[y] = int(item[y])
        nums2.append(item[1:])

# close the file
f.close()

# print the lists
print("Insert Sort")
print("The unsorted lists are: ")
for a in range(len(nums2)):
    print(nums2[a])

# sort the lists
for listS in nums2:
    insertsort(listS)

print("The sorted lists are: ")
for b in range(len(nums2)):
    print(nums2[b])

# store sorted lists in .txt output
fOut = open("insert.out", "w+")
for nLine2 in range(arraySize):
    number2 = nums2[nLine2]
    for x in range(len(number2)):
        fOut.write(str(number2[x]))
        fOut.write(" ")
    fOut.write("\n")
fOut.close()