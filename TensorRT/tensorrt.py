import tensorflow as tf
import tensorflow.contrib.tensorrt as trt
from tensorflow.python.platform import gfile

def load_model(sess, model_path):
    saver = tf.train.import_meta_graph(model_path)
    saver.restore(sess, model_path.replace('.meta', ''))

def convert_to_frozen_graph(sess, output_node_names):
    return tf.graph_util.convert_variables_to_constants(
        sess,
        tf.get_default_graph().as_graph_def(),
        output_node_names
    )

def save_frozen_graph(frozen_graph, output_path):
    with gfile.FastGFile(output_path, 'wb') as f:
        f.write(frozen_graph.SerializeToString())
    print(f"Frozen model is successfully stored at: {output_path}")

def create_trt_graph(frozen_graph, outputs, max_batch_size, max_workspace_size_bytes, precision_mode):
    return trt.create_inference_graph(
        input_graph_def=frozen_graph,
        outputs=outputs,
        max_batch_size=max_batch_size,
        max_workspace_size_bytes=max_workspace_size_bytes,
        precision_mode=precision_mode
    )

def save_trt_graph(trt_graph, output_path):
    with gfile.FastGFile(output_path, 'wb') as f:
        f.write(trt_graph.SerializeToString())
    print(f"TensorRT model is successfully stored at: {output_path}")

def main():
    # Configuration
    model_path = "./model/tensorflow/small/model_small.meta"
    frozen_graph_path = "./model/frozen_model.pb"
    trt_graph_path = "./model/TensorRT_model.pb"
    output_node_names = ["output_tensor/Softmax"]
    max_batch_size = 2
    max_workspace_size_bytes = 2 * (10**9)
    precision_mode = "FP32"

    # TensorFlow session configuration
    config = tf.ConfigProto(gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=0.50))

    with tf.Session(config=config) as sess:
        # Load the model
        load_model(sess, model_path)

        # Convert to frozen graph
        frozen_graph = convert_to_frozen_graph(sess, output_node_names)
        save_frozen_graph(frozen_graph, frozen_graph_path)

        # Create TensorRT graph
        trt_graph = create_trt_graph(
            frozen_graph,
            output_node_names,
            max_batch_size,
            max_workspace_size_bytes,
            precision_mode
        )
        save_trt_graph(trt_graph, trt_graph_path)

if __name__ == "__main__":
    main()