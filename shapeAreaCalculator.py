import Tkinter as tk
from decimal import *
from math import sqrt
class App():


	def __init__(self):
		self.shapes=[('Circle',1),('Triangle',2),('Square',3),('Pentagon',4),('Hexagon',5),('Heptagon',6),('Octagon',7),('Nonagon',8),('Decagon',9)]
		self.shapeSides=[1,3,4,5,6,7,8,9,10]
		self.root = tk.Tk()
		self.v = tk.IntVar()
		self.v.set(1)
		self.frame = tk.Frame(self.root)
		self.radioButtons()
		self.nextButton = tk.Button(self.frame, text = 'Next Step', width = 15, command = self.confirm)
		self.nextButton.pack()
		self.frame.pack()


	def radioButtons(self):
		for shape, val in self.shapes:
			self.radiobuttonoptions = tk.Radiobutton(self.frame, text=shape, indicatoron=0, width=20, padx=20, variable=self.v, command=self.checkShape, value=val).pack()
	
	def start(self):
		self.root.title('Shapes')
		self.root.mainloop()
		
	def confirm(self):
		self.sideCount = self.checkShape()
		self.frame.pack_forget()
		self.frame2 = tk.Frame(self.root)
		if self.sideCount == 1:
			self.label = tk.Label(self.frame2, text = 'Radius')
			self.entry = tk.Entry(self.frame2, width=25)
			self.label.pack(pady=20)
			self.entry.pack(pady=20)
		else:
			self.label = tk.Label(self.frame2, text = 'Side Length')
			self.entry = tk.Entry(self.frame2, width=25)
			self.label.pack(pady=20)
			self.entry.pack(pady=20)
		self.calculateButton = tk.Button(self.frame2, text = 'Calculate area', width = 15, command = self.calculate)
		self.calculateButton.pack(pady=20)
		self.frame2.pack()
		

	def calculate(self):
		sideLength = self.entry.get()
		l = float(sideLength)
 		a = shapeArea(self.sideCount, l)
 		self.frame2.pack_forget()
 		self.frame3 = tk.Frame(self.root)
 		self.areaLabel = tk.Label(self.frame3, text='Area is {}'.format(str(a)))
 		self.frame3.pack()
 		self.areaLabel.pack(padx=30, pady=30)
	

	def checkShape(self):
		sides = self.v.get()
		if sides == 1: return 1
		else:
			return sides+1

			
def shapeArea(shape, d):
	if shape == 1: return (3.141592654 * (d ** 2))

	elif shape == 3: return(((sqrt(3))/4) * (d**2))
	
	elif shape == 4: return(d**2)
	
	elif shape == 5: return((0.25 * (sqrt(5*(5+(2*(sqrt(5)))))))*(d**2))
	
	elif shape == 6: return((d**2) * ((3 * (sqrt(3)))/2))
	
	elif shape == 7: return(((7.0/4)*(d**2)*(2.0765)))
	
	elif shape == 8: return((2.0 * (d**2.0)) * (1.0 + sqrt(2.0)))
	
	elif shape == 9: return((9.0/4) * (2.747477422864) * (d ** 2.0))
	
	elif shape == 10: return((sqrt(5 + (2 * (sqrt(5))))) * (2.5) * (d**2))


def main():
	App().start()

if __name__ == '__main__':
	main()