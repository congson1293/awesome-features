#step 1 (with network or copy image to ur machine)
pip install wandb
docker pull wandb/local
# step 1' (copy image to ur machine)
docker load wandb/local
# step 2 (run)
docker run --rm -d -v wandb:/vol -p 8080:8080 --name wandb-local wandb/local
# step 3 create account and log in then copy api-key
# step 4: config
export WANDB_API_KEY=<api-key>
wandb login --host=http://localhost:8080

