# catalog what we already know
# define what median means
# the middle element of all the elements once they're sorted
# figure ou how to calculate it
# how do we eal with an even number of numbers?
# when should we handle sorting?


class MedianFetcher:
    def __init__(self):
        # define attributes on self
        self.median = None
        self.numbers = []

    # inserts the value n into our class
    def insert(self, n):
        # where to store n
        # maybe we store it in self.medan?
        # what happens when we insert more values?
        self.numbers.append(n)
        self.numbers.sort()  # sorts the list in place

    def get_median(self):
        if len(self.numbers) == 0:
            return None
        # fgure out if the length of the numbers list is odd or even
        mid = len(self.numbers) // 2  # // floors the number down. 1.5 = 1
        if len(self.numbers) % 2 == 1:
            # if its odd, then we can just pick the middle number
            # how do we get the middle number of a list?
            # take the length, divide it by 2
            return self.numbers[mid]
        else:
            # if it's even, get the avg of the 2 middle numbers
            # grab the element right before the mid element
            other = self.numbers[mid-1]
            return (other + self.numbers[mid])/2


medianFetcher = MedianFetcher()
medianFetcher.insert(5)
medianFetcher.insert(10)
print(medianFetcher.get_median())  # returns 7.5
medianFetcher.insert(100)
print(medianFetcher.get_median())  # return 10
