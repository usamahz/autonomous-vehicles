# Autonomous Vehicles: Computer Vision Implementation

This repository contains the implementation of various computer vision techniques for autonomous vehicles, including object detection, image classification, and segmentation using Convolutional Neural Networks (CNNs).

## Features

- **Object Detection:** Implementations of YOLOv3, YOLOv4, and their tiny versions for real-time object detection in autonomous driving scenarios.
- **Image Classification:** CNN models for classifying road signs, vehicles, and pedestrians.
- **Segmentation:** Advanced segmentation techniques for lane detection and road boundary identification.
- **Model Training and Evaluation:** Code for training and evaluating the CNN models on custom autonomous driving datasets.
- **Mobile Deployment:** Android app implementations for on-device inference in autonomous vehicles.

![CNN Architecture](https://github.com/usamahz/cnns/assets/39458672/a4d28f28-57a9-43e0-a5e0-e7249f507795)

## Getting Started

### Option 1: Using a Virtual Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/usamahz/autonomous-vehicles.git
   cd autonomous-vehicles
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Explore the code and run examples:
   ```bash
   python example.py
   ```

### Option 2: Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/usamahz/autonomous-vehicles.git
   cd autonomous-vehicles
   ```

2. Build the Docker image:
   ```bash
   docker build -t autonomous-vehicles .
   ```

3. Run the Docker container:
   ```bash
   docker run -it --gpus all autonomous-vehicles
   ```

4. Inside the container, you can now run the examples:
   ```bash
   python example.py
   ```

Note: Make sure you have Docker and NVIDIA Docker support installed if you're using a GPU.

## Usage

### Training:
   ```bash
   python train.py --dataset path/to/dataset --model yolov4
   ```

### Evaluation:
   ```bash
   python evaluate.py --dataset path/to/test_dataset --model yolov4
   ```

### Inference:
   ```bash
   python detect.py --image path/to/image.jpg --model yolov4
   ```

## Project Structure

The project includes implementations for YOLOv3, YOLOv4, and their tiny versions, as well as Android app implementations for on-device object detection in autonomous vehicles.

Key components:

1. YOLOv3 and YOLOv4 implementations for vehicle and pedestrian detection
2. Android app for real-time object detection in autonomous driving scenarios
3. Configuration files for model parameters
4. Evaluation scripts for model performance in autonomous driving contexts

## TensorRT Integration

This project includes TensorRT integration for optimized inference on NVIDIA GPUs. TensorRT is used to convert and optimize TensorFlow models for faster inference.

Key TensorRT-related files:
- `YOLOv3-YOLOv3Tiny/convert_trt.py`
- `YOLOv4-YOLOv4Tiny/convert_trt.py`

These scripts provide functionality to convert TensorFlow models to TensorRT-optimized models, supporting different precision modes (FP32, FP16, and INT8).

To convert a model to TensorRT format, use:

```
python convert_trt.py --weights ./checkpoints/yolov4-416 --quantize_mode float16 --output ./checkpoints/yolov4-trt-fp16-416
```

For benchmarking TensorRT models, refer to:
- `YOLOv3-YOLOv3Tiny/benchmarks.py`
- `YOLOv4-YOLOv4Tiny/benchmarks.py`

These benchmarking scripts allow you to compare the performance of TensorFlow, TensorRT, and TFLite models.

## Model Weights

Model weights for each implementation:
   - YOLOv1: Refer to [YOLOv1/README.md](YOLOv1/README.md) for weight download instructions.
   - YOLOv3 and YOLOv3-Tiny: Refer to [YOLOv3-YOLOv3Tiny/README.md](YOLOv3-YOLOv3Tiny/README.md) for weight download and conversion instructions.
   - YOLOv4 and YOLOv4-Tiny: Refer to [YOLOv4-YOLOv4Tiny/README.md](YOLOv4-YOLOv4Tiny/README.md) for weight download and conversion instructions.
   - MobileNet-SSD: Refer to [MobileNet-SSD/README.md](MobileNet-SSD/README.md) for model information.
   - Mask R-CNN: Refer to [Mask-RCNN/README.md](Mask-RCNN/README.md) for weight download instructions.

Each sub-README contains specific instructions on how to download and set up the weights for the respective models.

## Performance

The project includes evaluation metrics for object detection performance in autonomous driving scenarios. The mean Average Precision (mAP) is used as the primary metric. For detailed performance results, refer to the `assets/output.txt` file.

## Environment

The project uses a Conda environment. For a full list of dependencies, refer to the `environment.yml` file.

## Contributing

If you'd like to contribute to this autonomous vehicles project, please follow the standard GitHub fork and pull request workflow. Contributions, issues, and feature requests are welcome!

## License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2023 U S A M A H

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

