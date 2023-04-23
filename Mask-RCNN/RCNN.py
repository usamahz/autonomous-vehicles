import cv2 as cv
import argparse
import numpy as np
import os.path
import sys
from pathlib import Path
from imutils.video import FPS

file_path = Path.cwd()
out_file_path = Path(file_path / "test_out/")

confThreshold = 0.7
maskThreshold = 0.2
classes = []
colors = []


def choose_run_mode():
    global out_file_path
    if args.image:
        if not os.path.isfile(args.image):
            print("Input image file ", args.image, " doesn't exist")
            sys.exit(1)
        cap = cv.VideoCapture(args.image)

        out_file_path = str(out_file_path / (args.image[:-4] + '_out.jpg'))
    elif args.video:
        if not os.path.isfile(args.video):
            print("Input video file ", args.video, " doesn't exist")
            sys.exit(1)
        cap = cv.VideoCapture(args.video)
        out_file_path = str(out_file_path / (args.video[:-4] + '_out.mp4'))
    else:
        cap = cv.VideoCapture(0)
        out_file_path = str(out_file_path / 'webcam_out.mp4')
    return cap


def load_coco_classes():
    classes_file = str(file_path/"model/mscoco_labels.names")
    global classes
    with open(classes_file, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')


def load_colors():
    colors_file = str(file_path/"model/colors.txt")
    with open(colors_file, 'rt') as f:
        colors_str = f.read().rstrip('\n').split('\n')

    global colors
    for i in range(len(colors_str)):
        rgb = colors_str[i].split(' ')
        color = np.array([float(rgb[0]), float(rgb[1]), float(rgb[2])])
        colors.append(color)


def load_pretrain_model():
    text_graph = str(
        file_path/'model/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt')
    model_weights = str(file_path/"model/frozen_inference_graph.pb")
    net = cv.dnn.readNetFromTensorflow(model_weights, text_graph)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_OPENCL)
    return net


def set_video_writer(cap, write_fps=25):
    vid_writer = cv.VideoWriter(out_file_path, cv.VideoWriter_fourcc(*'mp4v'), write_fps,
                                (round(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
                                 round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
    return vid_writer


def visualize(boxes, masks):
    num_detections = boxes.shape[2]

    for i in range(num_detections):
        box = boxes[0, 0, i]
        pre_mask = masks[i]
        score = box[2]

        if score > confThreshold:
            class_id = int(box[1])
            left = int(origin_w * box[3])
            top = int(origin_h * box[4])
            right = int(origin_w * box[5])
            bottom = int(origin_h * box[6])

            left = max(0, min(left, origin_w-1))
            top = max(0, min(top, origin_h-1))
            right = max(0, min(right, origin_w-1))
            bottom = max(0, min(bottom, origin_h-1))

            pre_mask = pre_mask[class_id]

            draw_box_mask(frame, class_id, score, left,
                          top, right, bottom, pre_mask)


def draw_box_mask(frame, class_id, conf, left, top, right, bottom, pre_mask):
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    class_label = '%.2f' % conf
    if classes:
        assert(class_id < len(classes))
        class_label = '%s:%s' % (classes[class_id], class_label)
    label_size, base_line = cv.getTextSize(
        class_label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, label_size[1])
    cv.rectangle(frame, (left, top - round(1.5*label_size[1])), (left + round(1.5*label_size[0]), top + base_line),
                 (255, 255, 255), cv.FILLED)
    cv.putText(frame, class_label, (left, top),
               cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)
    mask = cv.resize(pre_mask, (right - left + 1, bottom - top + 1))
    mask_bool = (mask > maskThreshold)
    roi = frame[top: bottom+1, left: right+1][mask_bool]

    color = colors[class_id % len(colors)]
    frame[top:bottom+1, left:right+1][mask_bool] = (
        [0.3 * color[0], 0.3 * color[1], 0.3 * color[2]] + 0.7 * roi).astype(np.uint8)
    mask = mask_bool.astype(np.uint8)
    contours, hierarchy = cv.findContours(
        mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame[top: bottom+1, left: right+1],
                    contours, -1, color, 3, cv.LINE_8, hierarchy, 2)


def show_status(frame):
    t, _ = net.getPerfProfile()
    inf_label = 'Inference time: %.2f ms' % (
        t * 1000.0 / cv.getTickFrequency())
    cv.putText(frame, inf_label, (0, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    if not args.image:
        fps.update()
        fps.stop()
        fps_label = "FPS: {:.2f}".format(fps.fps())
        cv.putText(frame, fps_label, (0, 40),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Mask-RCNN object detection and segmentation')
    parser.add_argument('--image', help='Path to image file')
    parser.add_argument('--video', help='Path to video file.')
    args = parser.parse_args()

    cap = choose_run_mode()
    load_coco_classes()
    load_colors()
    net = load_pretrain_model()
    fps = FPS().start()
    video_writer = set_video_writer(cap)
    while cv.waitKey(1) < 0:
        has_frame, frame = cap.read()
        if not has_frame:
            print("Output file is stored as ", out_file_path)
            cv.waitKey(3000)
            break
        origin_h, origin_w = frame.shape[:2]
        blob = cv.dnn.blobFromImage(frame, swapRB=True, crop=False)
        net.setInput(blob)
        boxes, masks = net.forward(['detection_out_final', 'detection_masks'])
        visualize(boxes, masks)
        show_status(frame)
        if args.image:
            cv.imwrite(out_file_path, frame.astype(np.uint8))
        else:
            video_writer.write(frame.astype(np.uint8))

        windowName = 'Object-detection and Segmentation using Mask-RCNN'
        cv.imshow(windowName, frame)

    if not args.image:
        video_writer.release()
        cap.release()
    cv.destroyAllWindows()
