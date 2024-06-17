from pycocotools.coco import COCO
from datetime import datetime
import requests
import os


'''
# fazer download do arquivo 'annotations_trainval2017.zip' no link https://cocodataset.org/#download
e extrair o arquivo 'instances_train2017.json' para o mesmo diretório que esse script

# instalar a biblioteca pycocotools => pip install pycocotools

# por as classes que deseja baixar no dicionario classes_download abaixo junto com a quantidade de imagens 
que deseja baixar, por -1 caso deseja baixar todas disponíveis
'''


# para consulta ou caso quueira baixar todas as classes
all_claases = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 
'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 
'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 
'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 
'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 
'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 
'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 
'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 
'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 
'hair drier', 'toothbrush']


cwd = os.getcwd()
instacens_json_path = os.path.join(cwd, 'instances_train2017.json')
dest_dataser_folder = os.path.join(cwd, f'COCO_train2017_dataset_{datetime.now().strftime("%Y-%m-%d")}')
# Para baixar todas as imagens de todas as classes:
#	classes_download = {class: -1 for class in all_claases}
classes_download = {'car': 10, 'airplane': 15, 'keyboard': 10}


def main() -> None:
	coco = COCO(instacens_json_path)
	
	for class_id, num_imgs_download in classes_download.items():
		
		catIds = coco.getCatIds(catNms=[class_id])

		imgIds = coco.getImgIds(catIds=catIds)
		images = coco.loadImgs(imgIds)

		class_dir = os.path.join(dest_dataser_folder, class_id)
		os.makedirs(class_dir, exist_ok=True)
		
		if num_imgs_download == -1:
			num_imgs_download = len(images)
		print(f'# Found {len(images)} images of class \'{class_id}\' - downloading {num_imgs_download} images into folder \'{class_dir}\'')

		#Save the images into a local folder
		for im in images[:num_imgs_download]:
		    img_data = requests.get(im['coco_url']).content
		    img_dest_path = os.path.join(class_dir, im['file_name'])
		    with open(img_dest_path, 'wb') as handler:
		        handler.write(img_data)


if __name__  == '__main__':
	main()

