"""Process the downloaded MNIST dataset.

This script turn the raw MNIST datasets into processed-ready-to-be-used for training data.
"""

import numpy as np
import os

def process_mnist(raw_dir):
    # Read files
    with open(os.path.join(raw_dir, 'train-labels-idx1-ubyte'), 'rb') as f:
        y_train = np.frombuffer(f.read(), dtype=np.uint8, offset=8)
    with open(os.path.join(raw_dir, 'train-images-idx3-ubyte'), 'rb') as f:
        x_train = np.frombuffer(f.read(), dtype=np.uint8, offset=16).reshape(len(y_train), 28, 28)
        
    with open(os.path.join(raw_dir, 't10k-labels-idx1-ubyte'), 'rb') as f:
        y_test = np.frombuffer(f.read(), dtype=np.uint8, offset=8)
    with open(os.path.join(raw_dir, 't10k-images-idx3-ubyte'), 'rb') as f:
        x_test = np.frombuffer(f.read(), dtype=np.uint8, offset=16).reshape(len(y_test), 28, 28)

    # Normalize pixel values 0-1
    x_train = x_train.astype(np.float32) / 255.0
    x_test = x_test.astype(np.float32) / 255.0

    return x_train, y_train, x_test, y_test

# Execute
raw_path = './data/raw'
x_train, y_train, x_test, y_test = process_mnist(raw_path)

# Save processed state
np.savez_compressed('./data/processed/mnist_processed.npz', 
                    x_train=x_train, y_train=y_train, 
                    x_test=x_test, y_test=y_test)
