import subprocess
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--tpu-name', type=str, required=True)
parser.add_argument('--zone', type=str, required=True)
parser.add_argument('--accelerator-type', type=str, required=True)
parser.add_argument('--version', type=str, required=True)
parser.add_argument('--gcloud-init', action='store_true')

opt = parser.parse_args()

# init gcloud project
if opt.gcloud_init:
    subprocess.Popen('gcloud init', shell=True)

validate_str = f'Created tpu [{opt.tpu_name}]'

count = 1

while True:
    # create tpu-vm node
    print(f'\rCreating tpu-vm {opt.tpu_name} node {count}-th ...', end='', flush=True)

    p = subprocess.Popen(f"gcloud alpha compute tpus tpu-vm create {opt.tpu_name} "
                         f"--zone {opt.zone} "
                         f"--accelerator-type {opt.accelerator_type} "
                         f"--version {opt.version}", shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    p.wait()

    data = p.stdout.read()
    data = data.decode('utf-8')

    if 'ERROR:' in data and 'ALREADY_EXISTS:' in data:
        print(data)
        break
    elif validate_str in data:
        print(f'\n{validate_str}')
        break

    count += 1

    time.sleep(5)
