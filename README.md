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

## Performance

The project includes evaluation metrics for object detection performance in autonomous driving scenarios. The mean Average Precision (mAP) is used as the primary metric. For detailed performance results, refer to the `assets/output.txt` file.

## Environment

The project uses a Conda environment. For a full list of dependencies, refer to the `environment.yml` file.

## Contributing

If you'd like to contribute to this autonomous vehicles project, please follow the standard GitHub fork and pull request workflow. Contributions, issues, and feature requests are welcome!

## License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2023 [Your Name or Organization]

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
