# Based on imgproc.py
# Requires only pygame

import pygame
import pdb
		
class Viewer:
	def __init__(self, width=160, height=120, title="Pygame Image Processing"):
		pygame.init()
		pygame.display.quit()
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)
		pygame.display.flip()
		
	def displayImage(self, img):
		try:
			pygame.display.set_mode((img.width, img.height))
			self.screen.blit(img.image, (0,0))
			pygame.display.update()
		except:
			return None

class Image:
	def __init__(self,file_path=None, width=0, height=0):
		try:
			self.image = pygame.image.load(file_path)
		except:
			raise IOError
		self.width = self.image.get_size()[0]
		self.height = self.image.get_size()[1]
		
	def copy(self):
		return Image(0, 0, self.file_path)

	def __getitem__(self, key):
		x, y = key
		internal_pxarray = pygame.PixelArray(self.image)
		rgb_int = internal_pxarray[x][y]
		rgb = self.image.unmap_rgb(rgb_int)
		if len(rgb) == 4:
			return rgb[:-1]
		elif len(rgb) == 3:
			return rgb
		else:
			return None
		del internal_pxarray

	def __setitem__(self, key, value):
		internal_pxarray = pygame.PixelArray(self.image)
		x, y = key
		internal_pxarray[x][y] = value
		self.image = internal_pxarray.make_surface()
		del internal_pxarray
		
def timeWait(ms):
	pygame.time.wait(ms)

def waitTime(ms):
	pygame.time.wait(ms)
