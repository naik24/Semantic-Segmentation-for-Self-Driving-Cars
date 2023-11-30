# Semantic Segmentation for Self-Driving Cars

Semantic segmentation is a deep learning algorithm that associates a label or category with every pixel in an image. It is used to recognize a collection of pixels that form distinct categories. For example, an autonomous vehicle needs to identify vehicles, pedestrians, traffic signs, pavement, and other road features.

## Data
The dataset provides data images and labeled semantic segmentations captured via CARLA self-driving car simulator. The data was generated as part of the Lyft Udacity Challenge. The data has 5 sets of 1000 images and corresponding labels. Both the images and masks are of size 256 x 256. The file structure is as shown below.
```
dataA
│   ├── dataA
│       ├── CameraRGB
|       ├── CameraSeg
dataB
│   ├── dataB
│       ├── CameraRGB
|       ├── CameraSeg
dataC
│   ├── dataC
│       ├── CameraRGB
|       ├── CameraSeg
dataD
│   ├── dataD
│       ├── CameraRGB
|       ├── CameraSeg
dataE
    ├── dataE
        ├── CameraRGB
        ├── CameraSeg
```
<p align = center><img src = "https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/bf959144-d533-44d4-8399-cba2c70d8693"</p>

## U-Net Model

<p align = "center"><img src="https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/b987ad37-c689-4412-87f2-1712ee9799ed"></p>

Each blue box corresponds to a multi-channel feature map. The number of channels is denoted on top of the box. The x-y-size is provided at the lower left edge of the box. White boxes represent copied feature maps. The arrows denote the different operations.

## Training Parameters

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Metrics: Accuracy
- Epochs: 20
