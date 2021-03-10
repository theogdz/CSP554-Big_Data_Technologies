from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (user,movieId,rating,reviewId) = line.split(',')
        yield user , 1

    def combiner(self, user, counts):
        yield user, sum(counts)

    def reducer(self, user, counts):
        yield user, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()