# that is pillow module
from tkinter import *
from PIL import ImageTk, Image
from utils import load_image_paths,open_image_tnkr
import time

dir = 'test/other'
default_label = 'other'
file_save = "other_labels.csv"
width,height = 250,250
file_writer = open(file_save,'a')

label_dict = {}

def label_image(image="path",label = "label"):
	label_dict[image]= label
	# line = image+","+label+"\n"

def write_file():
	a = label_dict
	for k in sorted(label_dict.keys()):
		line = k+","+label_dict[k]+"\n"
		file_writer.write(line)
	file_writer.close()
	print("end")

def quit():
	write_file()
	root.quit()
	
def forward(img_no):

	# GLobal variable so that we can have
	# access and change the variable
	# whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	global img
	global button_bikni
	global button_other
	global button_sexyselfie
	global button_porn
	label.grid_forget()

	# This is for clearing the screen so that
	# our next image can pop up
	image_path = image_paths[img_no - 1]
	img = open_image_tnkr(image_path,width,height)
	# time.sleep(1)
	label = Label(root,image=img)
	label_image(image_path,default_label)
	# as the list starts from 0 so we are
	# subtracting one
	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="forward",command=lambda: forward(img_no+1))

	# img_no+1 as we want the next image to pop up
	if img_no == 4:
		button_forward = Button(root, text="Forward",state=DISABLED)

	# img_no-1 as we want previous image when we click
	# back button
	button_back = Button(root, text="Back",
	                 command=lambda: back(img_no-1))
	
	button_bikni = Button(root, text="bikini",
                        command=lambda: label_image(image =image_path, label = 'bikini'))
	button_other = Button(root, text="other",
	                        command=lambda: label_image(image =image_path,label = 'other'))
	button_sexyselfie = Button(root, text="sexyselfie",
	                        command=lambda: label_image(image =image_path,label = 'sexyselfie'))
	button_porn = Button(root, text="porn",
	                        command=lambda: label_image(image =image_path,label = 'porn'))


	# Placing the button in new grid
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)
	button_bikni.grid(row=7, column=0)
	button_other.grid(row=7, column=1)
	button_sexyselfie.grid(row=7, column=2)
	button_porn.grid(row=7, column=3)

 
def back(img_no):
 
	# We will have global variable to access these
	# variable and change whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	global button_bikni
	global button_other
	global button_sexyselfie
	global button_porn
	global img
	label.grid_forget()

	# for clearing the image for new image to pop up
	image_path = image_paths[img_no - 1]
	img = open_image_tnkr(image_path,width,height)
	label = Label(image=img)
	label.grid(row=1, column=0, columnspan=3)

	button_bikni.grid_forget()
	button_other.grid_forget()
	button_sexyselfie.grid_forget()
	button_porn.grid_forget()
	button_forward = Button(root, text="forward",
	                        command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Back",
	                     command=lambda: back(img_no - 1))
	button_bikni = Button(root, text="bikini",
                        command=lambda: label_image(image =image_path, label = 'bikini'))
	button_other = Button(root, text="other",
	                        command=lambda: label_image(image =image_path, label= 'other'))
	button_sexyselfie = Button(root, text="sexyselfie",
	                        command=lambda: label_image(image =image_path,label = 'sexyselfie'))
	button_porn = Button(root, text="porn",
	                        command=lambda: label_image(image =image_path,label = 'porn'))

	print(img_no)

	# whenever the first image will be there we will
	# have the back button disabled
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)

	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_forward.grid(row=5, column=2)
	button_bikni.grid(row=7, column=0)
	button_other.grid(row=7, column=1)
	button_sexyselfie.grid(row=7, column=2)
	button_porn.grid(row=7, column=3)
	
 
 
# Calling the Tk (The initial constructor of tkinter)
root = Tk()
 
# We will make the title of our app as Image Viewer
root.title("Image Viewer")
 
# The geometry of the box which will be displayed
# on the screen
root.geometry("700x700")
 
# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images
WIDTH =250
HEIGHT =250

image_paths = load_image_paths(dir,file_save)
# image_no_1 = ImageTk.PhotoImage(Image.open("data/bikini.jpg").resize((WIDTH, HEIGHT)))
# image_no_2 = ImageTk.PhotoImage(Image.open("data/nude.jpg").resize((WIDTH, HEIGHT)))
# image_no_3 = ImageTk.PhotoImage(Image.open("data/other.jpg").resize((WIDTH, HEIGHT)))
# image_no_4 = ImageTk.PhotoImage(Image.open("data/sexy_selfie.jpg").resize((WIDTH, HEIGHT)))
 
# List of the images so that we traverse the list
# List_images = [image_no_1, image_no_2, image_no_3, image_no_4]
img = open_image_tnkr("start.png",width,height)
label = Label(root,image=img)
 
# We have to show the box so this below line is needed
label.grid(row=1, column=0, columnspan=3)
 
# We will have three button back ,forward and exit
button_back = Button(root, text="Back", command=back,
                     state=DISABLED)
 
# root.quit for closing the app
button_exit = Button(root, text="Exit",
                     command=lambda: quit())
 
button_forward = Button(root, text="Forward",
                        command=lambda: forward(1))
 
button_bikni = Button(root, text="bikini",
                        command=lambda: label_image())
button_other = Button(root, text="other",
                        command=lambda: label_image())
button_sexyselfie = Button(root, text="sexyselfie",
                        command=lambda: label_image())
button_porn = Button(root, text="porn",
                        command=lambda: label_image())

# grid function is for placing the buttons in the frame
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)
button_bikni.grid(row=7, column=0)
button_other.grid(row=7, column=1)
button_sexyselfie.grid(row=7, column=2)
button_porn.grid(row=7, column=3)
 
root.mainloop()