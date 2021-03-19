from tensorflow import keras
from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()

try:
    from tensorflow.python.compiler.mlcompute import mlcompute
    mlcompute.set_mlc_device(device_name='cpu')
except:
    pass

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
keras.layers.Flatten(input_shape=(28, 28)),
keras.layers.Dense(2000, activation='relu'),
keras.layers.Dense(2000, activation='relu'),
keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'],run_eagerly=False)

model.fit(train_images, train_labels, epochs=1, batch_size=32)

