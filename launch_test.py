import wandb
import os
import time


wandb.init()

print('launch test!')
print('sleeping.......')
time.sleep(5)
print('awake!')

import platform
print('@@@@@@', platform.system(), platform.release(), platform.linux_distribution())