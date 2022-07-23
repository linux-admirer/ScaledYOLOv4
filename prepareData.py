import os

from dataformats import BDD,YOLO

def _convertBDDtoYOLO(config) -> bool:
	if config["datasets"] != "BDD":
		print("Unknown Dataset")
		return False
		
	bdd = BDD()
	yolo = YOLO(os.path.abspath(config["cls_list"]))

	success, data = bdd.parse(config["label"], config["img_path"])
	if not success:
		print("BDD Parsing Result : {}, msg : {}".format(success, data))
		return False

	success, data = yolo.generate(data)
	if not success:
		print("YOLO Generating Result : {}, msg : {}".format(success, data))
		return False
		
	success, data = yolo.save(data, config["output_path"], config["img_path"],
							config["img_type"], config["manifest_path"])
	if success:
		print("Saving Result : {}, msg : {}".format(success, data))
	return success


def _deleteFile(filePath):
	if os.path.isfile(filePath):
		os.remove(filePath)
	else:
		print("{} is not a file".format(filePath))


def _removeImagesWithoutLabel(config):
	outputLabelDir = config["output_path"]
	imagesDir = config["img_path"]

	imagesFound = {}
	for filename in os.listdir(outputLabelDir):
		imagesFound[os.path.splitext(filename)[0]] = True
	for filename in os.listdir(imagesDir):
		filenameWithoutExt = os.path.splitext(filename)
		if not filenameWithoutExt in imagesFound:
			_deleteFile(os.path.join(imagesDir, filename))


def prepareBDDData(config):
	_convertBDDtoYOLO(config)
	_removeImagesWithoutLabel(config)
