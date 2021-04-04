import os, time
import sys
import visual


sys.path.append(os.path.dirname(__file__) + "/../")

from scipy.misc import imread

from nnet import predict
from util import visualize
from util.config import load_config
from dataset.pose_dataset import data_to_input


cfg = load_config("demo/pose_cfg.yaml")

# Load and setup CNN part detector
sess, inputs, outputs = predict.setup_pose_prediction(cfg)

# Read image from file
di='D:/time/'  
li=os.listdir(di)  
li.sort() 
for key in li:
	image = imread((di+key), mode='RGB')
	startTime=time.time()  

	#file_name = "demo/image.png"
	#image = imread(file_name, mode='RGB')

	image_batch = data_to_input(image)

	# Compute prediction with the CNN
	outputs_np = sess.run(outputs, feed_dict={inputs: image_batch})
	scmap, locref, _ = predict.extract_cnn_output(outputs_np, cfg)

	# Extract maximum scoring location from the heatmap, assume 1 person
	pose = predict.argmax_pose_predict(scmap, locref, cfg.stride)

	# Visualise
	visual.visualize_joints(image, pose, key, di)
	runtime=time.time()-startTime
	print ("本帧 ", key, " 预测耗时 ", runtime, "m秒") 


