import os

from dataformats import BDD,YOLO

def convertBDDtoYOLO(dict:config) -> bool:
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
