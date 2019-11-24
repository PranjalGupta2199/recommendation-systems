import latent_factor as lf
from latent_factor.model import LatentFactor
import time

if __name__ == "__main__":
    model = LatentFactor(k=50, epoch=70, beta=0.1, alpha=0.01)
    model.train()
    print("Validation Dataset {}".format(
        model.get_mean_abs_error(model.validation_dataset)))
    print("Validation Dataset {}\n\n".format(
        model.get_rms_error(model.validation_dataset)))