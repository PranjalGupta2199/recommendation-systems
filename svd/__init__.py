import os
from svd import model
from svd import preprocessor
from svd import database

if not os.path.exists('./svd/binaries'):
    os.makedirs("./svd/binaries")
