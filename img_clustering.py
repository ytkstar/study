import os.path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import manifold
from matplotlib.pyplot import imread
from glob import iglob #glob.iglobでもOK

store = 'images'

image_data = []
for filename in iglob(os.path.join(store, '*jpg')):
    image_data.append(imread(filename))

img_np_orig = np.array(image_data)
img_np = img_np_orig.reshape(img_np_orig.shape[0], -1)
#print(image_np)

def plot_embedding(X, img_np_orig):
    #リスケールする
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X- x_min) / (x_max - x_min)

    #t-SNEの位置に従って画像をグラフ化
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    for i in range(img_np.shape[0]):
        imagebox = offsetbox.AnnotationBbox(
            offsetbox = offsetbox.OffsetImage(img_np_orig[i], zoom = .1),
            xy = X[i],
            frameon = False
        )
        ax.add_artist(imagebox)

tsne = manifold.TSNE(n_components = 2, init = 'pca')
X_tsne = tsne.fit_transform(img_np)

plot_embedding(X_tsne, img_np_orig)
plt.show()