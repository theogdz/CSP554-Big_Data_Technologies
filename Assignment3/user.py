from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (userID,movieID,rating,timestamp) = line.split(',')
        yield userID , 1

    def combiner(self, userID, counts):
        yield userID, sum(counts)

    def reducer(self, userID, counts):
        yield userID, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()