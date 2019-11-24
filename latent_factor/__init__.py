import os
from latent_factor import config, model, preprocessor

if not os.path.exists('./latent_factor/binaries'):
    os.makedirs("./latent_factor/binaries")
