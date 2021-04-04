# Installation

```shell
## install tensorflow and its dependencies
pip3 install --upgrade tensorflow
pip3 install scipy scikit-image matplotlib pyyaml easydict cython munkres

## install pre-trained model
${workpath}\models\mpii\download_models.sh

```

# Run

```shell
# windows os 
set TF_CUDNN_USE_AUTOTUNE=0 

# single image prediction
python .\singleperson.py

# series of image prediciton 
python .\singleperson-test.py

# generation gif 
python .\imppt.py

```