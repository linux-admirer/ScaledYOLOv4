trainConfig ={
	"datasets": "BDD",
	"img_path": "../bdd100k/images/100k/train",
	"label": "../bdd100k/labels/det_train.json",
	"img_type": ".jpg",
	"manifest_path": "./",
	"output_path": "../bdd100k/labels/train/",
	"cls_list": "data/bdd100k.names",
}
validationConfig ={
	"datasets": "BDD",
	"img_path": "../bdd100k/images/100k/val",
	"label": "../bdd100k/labels/det_val.json",
	"img_type": ".jpg",
	"manifest_path": "./",
	"output_path": "../bdd100k/labels/val/",
	"cls_list": "data/bdd100k.names",
}

import BDDtoYOLO
convertBDDtoYOLO(trainConfig)
convertBDDtoYOLO(validationConfig)
