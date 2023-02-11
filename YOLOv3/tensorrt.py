# import the needed libraries
import tensorflow as tf
import tensorflow.contrib.tensorrt as trt
from tensorflow.python.platform import gfile




with tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=0.50))) as sess:
    # import the meta graph of the tensorflow model
    #saver = tf.train.import_meta_graph("./model/tensorflow/big/model1.meta")
    saver = tf.train.import_meta_graph("./model/tensorflow/small/model_small.meta")
    # then, restore the weights to the meta graph
    #saver.restore(sess, "./model/tensorflow/big/model1")
    saver.restore(sess, "./model/tensorflow/small/model_small")
    
    # specify which tensor output you want to obtain 
    # (correspond to prediction result)
    your_outputs = ["output_tensor/Softmax"]
    
    # convert to frozen model
    frozen_graph = tf.graph_util.convert_variables_to_constants(
        sess, # session
        tf.get_default_graph().as_graph_def(),# graph+weight from the session
        output_node_names=your_outputs)
    #write the TensorRT model to be used later for inference
    with gfile.FastGFile("./model/frozen_model.pb", 'wb') as f:
        f.write(frozen_graph.SerializeToString())
    print("Frozen model is successfully stored!")
    
trt_graph = trt.create_inference_graph(
    input_graph_def=frozen_graph,# frozen model
    outputs=your_outputs,
    max_batch_size=2,# specify your max batch size
    max_workspace_size_bytes=2*(10**9),# specify the max workspace
    precision_mode="FP32") # precision, can be "FP32" (32 floating point precision) or "FP16"

#write the TensorRT model to be used later for inference
with gfile.FastGFile("./model/TensorRT_model.pb", 'wb') as f:
    f.write(trt_graph.SerializeToString())
print("TensorRT model is successfully stored!")