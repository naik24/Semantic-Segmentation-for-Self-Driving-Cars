# Semantic Segmentation for Self-Driving Cars

Semantic segmentation is a deep learning algorithm that associates a label or category with every pixel in an image. It is used to recognize a collection of pixels that form distinct categories. For example, an autonomous vehicle needs to identify vehicles, pedestrians, traffic signs, pavement, and other road features.

## Data
The dataset provides data images and labeled semantic segmentations captured via <a href = "https://carla.org/">CARLA</a> self-driving car simulator. The data was generated as part of the Lyft Udacity Challenge. The data has 5 sets of 1000 images and corresponding labels. Both the images and masks are resized to 256 x 256. The dataset is available on <a href = "https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge">Kaggle</a>.
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
<p align = center><img src = "https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/3b4d503f-3d40-499c-b09f-4c0b565e80e2"</p>


## U-Net Model

<p align = "center"><img src="https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/a9fca134-f939-4065-baa5-a5b8d3a1041d"></p>


Each blue box corresponds to a multi-channel feature map. The number of channels is denoted on top of the box. The x-y-size is provided at the lower left edge of the box. White boxes represent copied feature maps. The arrows denote the different operations. Link to the paper <a href = "https://arxiv.org/pdf/1505.04597.pdf">here</a>.
