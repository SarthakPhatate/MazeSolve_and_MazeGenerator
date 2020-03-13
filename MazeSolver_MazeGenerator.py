# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog as tkFileDialog
import cv2
import task_1a as t
import image_enhancer
import maze_generator
from tkinter import simpledialog

def generate_image():
    name = simpledialog.askstring(title="Maze Generator",prompt="Enter image name")
    maze_generator.run(name)
    
def select_image():
	# grab a reference to the image panels
	global panelA, panelB

	# open a file chooser dialog and allow the user to select an input
	# image
	path = tkFileDialog.askopenfilename()

	# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = t.readImage(path)

		shortestPath = t.solveMaze(image, (0,0), (19,19), 20, 20)
		img = image_enhancer.highlightPath(image, (0,0), (19,19), shortestPath)

		# convert the images to PIL format...
		image = Image.fromarray(image)
		edged = Image.fromarray(img)

		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)

		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)

			# while the second panel will store the edge map
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)

		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged

# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
root.title("Maze Solver")
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Generate maze", command=generate_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

btn1 = Button(root, text="Select an image", command=select_image)
btn1.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

# kick off the GUI
root.mainloop()
