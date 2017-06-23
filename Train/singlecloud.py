from wordcloud import *
import matplotlib.pyplot as plt
from scipy.misc import imread
from PIL import Image

def generate_img(tag, img_name, back_image):
	data = ' '.join(tag)
	# im = Image.open("01.png")
	# Lim = im.convert('L')
	# Lim.save("01_grey.png")
	mask_img = imread(back_image, flatten=True)
	wordcloud = WordCloud(font_path='msyh.ttc',background_color='white',mask=mask_img,random.order=T,colors=c('red','organize','yellow')).generate(data)
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.savefig(img_name, dpi=600)