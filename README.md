# Semantic Segmentation for Self-Driving Cars

Semantic segmentation is a deep learning algorithm that associates a label or category with every pixel in an image. It is used to recognize a collection of pixels that form distinct categories. For example, an autonomous vehicle needs to identify vehicles, pedestrians, traffic signs, pavement, and other road features.

## Data
The dataset provides data images and labeled semantic segmentations captured via <a href = "https://carla.org/">CARLA</a> self-driving car simulator. The data was generated as part of the Lyft Udacity Challenge. The data has 5 sets of 1000 images and corresponding labels. Both the images and masks are resized to 256 x 256. The ouput labels have 13 classes in total:
- 0: None
- 1: Buildings
- 2: Fences
- 3: Other
- 4: Pedestrians
- 5: Poles
- 6: Roadlines
- 7: Roads
- 8: Sidewalks
- 9: Vegetation
- 10: Vehicles
- 11: Walls
- 12: TrafficSigns

The dataset is available on <a href = "https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge">Kaggle</a>.
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

## Dataset Distribution
The 5000 images and their corresponding are distributed into train, validation, and test sets as described below:
- Train: 4000
- Validation: 800
- Test: 200

## U-Net Model

<p align = "center"><img src="https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/a9fca134-f939-4065-baa5-a5b8d3a1041d"></p>


Each blue box corresponds to a multi-channel feature map. The number of channels is denoted on top of the box. The x-y-size is provided at the lower left edge of the box. White boxes represent copied feature maps. The arrows denote the different operations. Link to the paper <a href = "https://arxiv.org/pdf/1505.04597.pdf">here</a>.

## Tools & Technologies
![image](https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/333e19cf-1174-43ce-a923-37f024e7a3a7)
![image](https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/35db5150-40a8-4fee-972a-01762b035411)
![image](https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/a6b463b9-ab19-4c9d-8eca-f266deebb71c)
![image](https://github.com/naik24/Semantic-Segmentation-for-Self-Driving-Cars/assets/69704762/246a3b8d-ee43-4290-90ea-f2dfad3af6f1)




