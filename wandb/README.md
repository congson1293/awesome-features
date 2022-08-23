# Use Wandb to run on computer without internet

## Setup
Refer to file ```wandb/setup.sh```

## Notes
1. Disable wandb to test

> export WANDB_MODE=disabled

2. Run in online mode

```wandb online```, ```WANDB_MODE=online``` or ```wandb.init(mode="online")``` - runs in online mode, the default

3. Runs in offline mode, writes all data to disk for later syncing to a server

```wandb offline```, ```WANDB_MODE=offline``` or ```wandb.init(mode="offline")``` 

4. Disable wandb

```wandb disabled```, ```WANDB_MODE=disabled``` or ````wandb.init(mode="disabled")```` 

- makes all calls to wandb api's noop's, while maintaining core functionality such as wandb.config and wandb.summary in case you have logic that reads from these dicts.

5. Enable wandb

```wandb enabled``` - sets the mode to back online