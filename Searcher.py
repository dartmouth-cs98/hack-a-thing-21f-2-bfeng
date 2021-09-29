import numpy as np
import csv

class Searcher:

	def __init__(self, indexPath):

        # store path to index file
		self.indexPath = indexPath

	def search(self, queryFeatures, limit = 10):

        # to store query results
        # key = imageID, value = distance from query image (dissimilarity)
		results = {}

		with open(self.indexPath) as f:

			reader = csv.reader(f)

			# loop over the rows in the index (each index image's feature vector)
			for row in reader:

                # compute chi-squared distance between query image and index image
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)

				results[row[0]] = d

			# close the reader
			f.close()

		# sort results
		results = sorted([(v, k) for (k, v) in results.items()])

        # return (limit) best results
		return results[:limit]

    # def chi2_distance(self, histA, histB, eps = 1e-10):
    #
    #     d = 0.5 * np.sum([(a - b) ** 2]) / (a + b + eps) for (a, b) in zip(histA, histB)])

	def chi2_distance(self, histA, histB, eps = 1e-10):

		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])

		return d
