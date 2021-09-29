from ColorDescriptor import ColorDescriptor
from Searcher import Searcher
import argparse
import cv2

# for parsing commandline arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize Descriptor object
cd = ColorDescriptor((8, 12, 3))

# load query image and describe
query = cv2.imread(args["query"])
features = cd.describe(query)

# search
searcher = Searcher(args["index"])
results = searcher.search(features, 4)

# display query
cv2.imshow("Query", query)

# loop over results and display them
count = 1
for (score, resultID) in results:
    # load the result image and display it
    print(resultID)
    result = cv2.imread(args["result_path"] + "/" + resultID)
    cv2.imshow("Result " + str(count), result)
    count += 1


cv2.waitKey(0)
