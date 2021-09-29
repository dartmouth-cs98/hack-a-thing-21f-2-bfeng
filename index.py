from ColorDescriptor import ColorDescriptor
import argparse
import glob
import cv2

# for parsing commandline argument
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True, help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize ColorDescriptor object
cd = ColorDescriptor((8, 12, 3))

# open output file
output = open(args["index"], "w")

# loop through each image path in provided dataset
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):

    # load image
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe image
	features = cd.describe(image)

	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

output.close()
