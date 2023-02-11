### Download the model files First

You can fork the _.ckpt_ weights model [here](https://drive.google.com/file/d/0B2JbaJSrWLpza08yS2FSUnV2dlE/view?usp=sharing) or [here](https://pan.baidu.com/s/1Acm1lSpnATymbtqpyBr0xg), thanks to [gliese581gg](https://github.com/gliese581gg/YOLO_tensorflow).  
Then place it to `weights` folder.

### Usage Examples :

Put the test file (image only) to `test_images` folder.  
 command line input: `python yolo.py` or `python yolo_tf.py`

### Note

Two scripts here provided are nearly same, for `yolo_tf.py` uses some **tf constructor API** methods for functions like _Non-max Minimum_, etc.
