### THIS IS A GIT ADDRESS
https://github.com/PoppyPoppyPiggy/yolo_server.git

### PIP LIST IN 
'/requirements.txt'

### DARKNET
git clone https://github.com/AlexeyAB/darknet.git
cd darknet
make

#### chore darknet/Makefile
GPU=1
CUDNN=1
OPENCV=1

### cuDNN 9.2.1 Download
wget https://developer.download.nvidia.com/compute/cudnn/9.2.1/local_installers/cudnn-local-repo-ubuntu2004-9.2.1_1.0-1_amd64.deb

sudo dpkg -i cudnn-local-repo-ubuntu2004-9.2.1_1.0-1_amd64.deb

sudo cp /var/cudnn-local-repo-ubuntu2004-9.2.1/cudnn-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update

sudo apt-get -y install cudnn

#### to install for cuda 11
sudo apt-get -y install cudnn-cuda-11

#### to install for cuda 12
sudo apt-get -y install cudnn-cuda-12

### cuda toolkit download 
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local

wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin

sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget https://developer.download.nvidia.com/compute/cuda/12.5.1/local_installers/cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb

sudo dpkg -i cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb

sudo cp /var/cuda-repo-wsl-ubuntu-12-5-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update

sudo apt-get -y install cuda-toolkit-12-5

### path
echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc

echo 'export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig' >> ~/.bashrc
source ~/.bashrc

### sudo content
sudo apt-get update
sudo apt-get install pkg-config
sudo chmod +x /usr/bin/pkg-config
sudo apt-get install libopencv-dev


## INTRO
THIS IS A PROJECT WHICH MAKE THE OBJECTION DETECTION MODEL OF
CAT AND DOG'S EYES AND SKIN DESESES

WHEN THE IMAGE CAME TO THIS MODEL, THEN THAT DO ANALYZE IT :)



