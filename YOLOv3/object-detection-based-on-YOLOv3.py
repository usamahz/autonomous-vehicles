import os
import cv2 as cv
import numpy as np
import argparse
import sys
from imutils.video import FPS

file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
outputFile = file_path + "test_out" + os.sep
confThreshold = 0.5  # Confidence threshold
nmsThreshold = 0.4   # Non-maximum suppression threshold
inpWidth, inpHeight = 416, 416       # Width & height of network's input image

# Usage example:  python object-detection-based-on-YOLOv3.py --video=run.mp4
parser = argparse.ArgumentParser(
    description='Object Detection using YOLO in OPENCV')
parser.add_argument('--image', help='Path to image file.')
parser.add_argument('--video', help='Path to video file.')
args = parser.parse_args()


def choose_run_mode():
    if args.image:
        # Open the image file
        if not os.path.isfile(args.image):
            print("Input image file ", args.image, " doesn't exist")
            sys.exit(1)
        cap = cv.VideoCapture(args.image)
        global outputFile
        outputFile += args.image[:-4] + '_out.jpg'
    elif args.video:
        # Open the video file
        if not os.path.isfile(args.video):
            print("Input video file ", args.video, " doesn't exist")
            sys.exit(1)
        cap = cv.VideoCapture(args.video)
        outputFile += args.video[:-4] + '_out.mp4'
    else:
        # Webcam input
        cap = cv.VideoCapture(0)
        outputFile += 'webcam_out.mp4'
    return cap


def get_coco_classes():
    # Load names of classes
    classes_path = file_path+'Model'+os.sep+'coco.names'
    # reading & text mode
    with open(classes_path, 'rt') as f:
        classes = f.read().split('\n')[:-1]
    return classes


def load_pretrain_model():
    # Give the configuration and weight files for the model and load the network using them.
    model_config = file_path + 'Model' + os.sep + 'yolov3.cfg'
    model_weights = file_path + 'Model' + os.sep + 'yolov3.weights'

    net = cv.dnn.readNetFromDarknet(model_config, model_weights)
    print('YOLOv3 darknet model loaded successfully')
    # cv.dnn.DNN_TARGET_OPENCL to run it on a GPU
    # current OpenCV version is tested only with Intel’s GPUs, it would automatically switch to CPU
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_OPENCL)
    return net


def get_output_layers(net):
    # Get the names of all the layers in the network
    layers_names = net.getLayerNames()
    print('layers_names=', layers_names)
    for i in net.getUnconnectedOutLayers():
        print('i=', i)
    # Get the names of the output layers,
    print('net.getUnconnectedOutLayers()=', net.getUnconnectedOutLayers())
    return [layers_names[i - 1] for i in net.getUnconnectedOutLayers()]


def remove_non_max_boxes(detections):
    class_ids, confidences, boxes = [], [], []
    for detection in detections:
        for tep in detection:
            scores = tep[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confThreshold:
                center_x, center_y = int(tep[0]*origin_w), int(tep[1]*origin_h)
                box_width, box_height = int(
                    tep[2]*origin_w), int(tep[3]*origin_h)
                box_left, box_top = int(
                    center_x - box_width/2), int(center_y - box_height/2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([box_left, box_top, box_width, box_height])
    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i
        box = boxes[i]
        x_start, y_start = box[0], box[1]
        x_end, y_end = x_start+box[2], y_start+box[3]
        draw_box_label(class_ids[i], confidences[i],
                       x_start, y_start, x_end, y_end)


def draw_box_label(class_id, confidence, x_start, y_start, x_end, y_end):
    cv.rectangle(frame, (x_start, y_start), (x_end, y_end), (255, 178, 50), 2)
    label = '{0}: {1:.2f}%'.format(classes[class_id], confidence * 100)
    label_size, base_line = cv.getTextSize(
        label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(y_start, label_size[1])
    cv.rectangle(frame, (x_start, top - round(1.2 * label_size[1])),
                 (x_start + round(1.5 * label_size[0]), top + base_line),
                 (255, 255, 255), cv.FILLED)
    cv.putText(frame, label, (x_start, top),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)


def show_status(frame):
    # Put efficiency information. The function getPerfProfile returns the
    # overall time for inference(t) and the timings for each of the layers(in layersTimes)
    t, _ = net.getPerfProfile()
    inf_label = 'Inference time: %.2f ms' % (
        t * 1000.0 / cv.getTickFrequency())
    cv.putText(frame, inf_label, (0, origin_h-50),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    if not args.image:
        fps.update()
        fps.stop()
        fps_label = "FPS: {:.2f}".format(fps.fps())
        cv.putText(frame, fps_label, (0, origin_h-25),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


if __name__ == '__main__':
    # choosing image/video/webcam
    cap = choose_run_mode()
    classes = get_coco_classes()
    # load YOLOv3 darknet model
    net = load_pretrain_model()

    fps = FPS().start()
    vid_writer = cv.VideoWriter(outputFile, cv.VideoWriter_fourcc(*'mp4v'), 30,
                                (round(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
                                 round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
    while cv.waitKey(1) < 0:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print("Output file is stored as ", outputFile)
            cv.waitKey(3000)
            break

        origin_h, origin_w = frame.shape[:2]
        # https://github.com/opencv/opencv/tree/master/samples/dnn
        blob = cv.dnn.blobFromImage(
            frame, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        # YOLOv3
        detections = net.forward(get_output_layers(net))
        #non_max_suppression, box
        remove_non_max_boxes(detections)
        # Inference timeFPS
        show_status(frame)

        # Write the frame with the detection boxes
        if args.image:
            cv.imwrite(outputFile, frame)
        else:

            vid_writer.write(frame)

        winName = 'YOLOv3 object detection in OpenCV'
        # cv.namedWindow(winName, cv.WINDOW_NORMAL)
        cv.imshow(winName, frame)

    if not args.image:
        vid_writer.release()
        cap.release()
    cv.destroyAllWindows()
