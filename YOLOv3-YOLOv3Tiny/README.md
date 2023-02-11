# Convert darknet weights to tensorflow
## yolov3
python save_model.py --weights ./data/yolov3.weights --output ./checkpoints/yolov3-416 --input_size 416 --model yolov3 

## yolov3-tiny
python save_model.py --weights ./data/yolov3-tiny.weights --output ./checkpoints/yolov3-tiny-416 --input_size 416 --model yolov3 --tiny

# Run demo tensorflow
python detect.py --weights ./checkpoints/yolov3-416 --size 416 --model yolov3 --image ./data/kite.jpg

python detect.py --weights ./checkpoints/yolov3-tiny-416 --size 416 --model yolov3 --image ./data/kite.jpg --tiny
