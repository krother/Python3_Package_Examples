
import numpy as np
from matplotlib import pyplot as plt
import wordcloud
import this

# store the Zen of Python in a string
text = ''.join([this.d.get(c, ' ') for c in this.s]).lower()

# leave a blank square in the cloud
mask = np.zeros((500, 500, 3), np.uint8)
mask[150:350,150:350,:] = 255

cloud = wordcloud.WordCloud(background_color="white",
                max_words=50,
                mask=mask,
                collocations=False,
                contour_color='steelblue').generate(text)

plt.figure(num = None, figsize = (8, 8))
plt.imshow(cloud, interpolation='bilinear')
plt.savefig('cloud.png')
