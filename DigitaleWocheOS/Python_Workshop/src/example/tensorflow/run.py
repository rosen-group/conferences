# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""label_image for tflite."""

import argparse
import time

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tensorflow as tf

def get_image(imgpath: str):
    if imgpath == 'dialog':
        root = tk.Tk()
        root.withdraw()

        return filedialog.askopenfilename()
    return imgpath

def plot_prediction(predictions: list, labels: list):
    top_k = predictions.argsort()[-5:][::-1]
    points = len(top_k)
    x = 0.5 + np.arange(points)
    y = [float(i) / 255.0 for i in [predictions[i] for i in top_k]]

    fig,ax = plt.subplots()

    fig.suptitle('Predictions')

    plt.subplots_adjust(bottom=0.32)
    
    bars = ax.bar(x, y, width = 1, edgecolor = "white", linewidth=0.7)
    ax.bar_label(bars)

    y_ticks = np.arange(0,1.1, step=0.25)

    ax.set(xlim=(0, points), 
           xticks=np.arange(1,points + 1), 
           xticklabels=[labels[i] for i in top_k], 
           xlabel='Race',
           ylim=(0, 1), yticks=y_ticks, 
           ylabel='probability')
    
    plt.xticks(rotation=45, ha='right')
    plt.show()


def load_labels(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--image',
        default='/tmp/grace_hopper.bmp',
        help='image to be classified')
    parser.add_argument(
        '-m',
        '--model_file',
        default='/tmp/mobilenet_v1_1.0_224_quant.tflite',
        help='.tflite model to be executed')
    parser.add_argument(
        '-l',
        '--label_file',
        default='/tmp/labels.txt',
        help='name of file containing labels')

    args = parser.parse_args()

    interpreter = tf.lite.Interpreter(
        model_path=args.model_file,
        num_threads=1)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # check the type of the input tensor
    floating_model = input_details[0]['dtype'] == np.float32

    # NxHxWxC, H:1, W:2
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    img =Image.open(get_image(args.image)).resize((width, height))

    # add N dim
    input_data = np.expand_dims(img, axis=0)

    if floating_model:
        input_data = (np.float32(input_data) - 127.5) / 127.5

    interpreter.set_tensor(input_details[0]['index'], input_data)

    start_time = time.time()
    interpreter.invoke()
    stop_time = time.time()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    results = np.squeeze(output_data)
    labels = load_labels(args.label_file)

    plot_prediction(results, labels)
