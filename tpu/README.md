## Setup TPU

### Installation
0. Install Gcloud

[How-to](https://cloud.google.com/sdk/docs/install)

1. (Optional) Delete TPU Node

Access link: https://console.cloud.google.com/compute/tpus?project=<project-name> to delete node

2. Create TPU VM

```python create_tpu_vm.py --zone=europe-west4-a --accelerator-type=v3-8 --version=tpu-vm-pt-2.0 --tpu-name <name>```

3. Setup for ready-to-run

Login: ```gcloud alpha compute tpus tpu-vm ssh <name> --zone europe-west4-a -- -L 5000:localhost:5000```

Setup: 
```
sudo killall -9 python3
sudo apt update && sudo apt -y upgrade 
sudo apt install jupyter jupyter-notebook 
pip3 install jupyter ipywidgets
jupyter nbextension enable --py widgetsnbextension
pip3 install --upgrade
pip3 install --upgrade pip
jupyter-notebook --port 5000
```

### Read More

1. [TPU Starter](https://github.com/ayaka14732/tpu-starter)