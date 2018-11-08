
# install the wordcloud package:
# pip install wordcloud

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import wordcloud
import re


lyrics = "she loves you yeah yeah yeah"


mask = np.zeros((500, 500, 3), np.uint8)
mask[150:350,150:350,:] = 255

# mask = np.array(Image.open('mroom.jpg'))

cloud = wordcloud.WordCloud(background_color="white",
                max_words=250,
                mask=mask,
                collocations=False,
                contour_color='steelblue').generate(lyrics) # <-- lyrics is a string


plt.figure(num = None, figsize = (40,40))
plt.imshow(cloud, interpolation='bilinear')
plt.savefig('cloud.png')
plt.show()
