import os
import sys
from PIL import ImageTk, Image
from glob import glob
import pandas as pd


def open_image_tnkr(image_path,width,height):

	img = ImageTk.PhotoImage(Image.open(image_path).resize((width, height)))

	return img

def load_image_paths(dir,csv_path):

	img_paths = sorted(glob(os.path.join(dir,"*")))

	if os.path.exists(csv_path):
		try:
			already_existing = pd.read_csv(csv_path,header=None)
			already_existing = list(already_existing[0])
			old_img_paths = img_paths
			img_paths =[]
			for p in old_img_paths:
				if p not in already_existing:
					img_paths.append(p)
		except:
			print("File is empty or problematic")
			pass

	if len(img_paths)<1:
		print("ALL Done")
		sys.exit()
	return img_paths
	

if __name__=="__main__":

	files = load_image_paths("data","check.csv")

	print(files)