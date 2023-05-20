import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digitos = load_digits()

plt.figure(figsize=(14,4))
for index, (imagem, rotulo) in enumerate(zip(digitos.data[0:5], digitos.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(imagem, (8,8)), cmap=plt.cm.gray)
    plt.title('Treinamento: {}\n'.format(rotulo, fontsize=15))
plt.show()