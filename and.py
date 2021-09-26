from utils.all_utils import createModel
import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename = os.path.join(log_dir,"running_logs.log"),level=logging.INFO, format=logging_str)


def main(data, eta, epoch, file_name, plot_name):
    createModel(data, eta, epoch, file_name, plot_name)

    

if __name__ == '__main__': ##entry point
    AND = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0, 0, 0, 1]
    }

    ETA = 0.3 # learning rate between 0 and 1 (assume)
    EPOCHS = 10

    
    try:
        main(data=AND, eta=ETA, epoch=EPOCHS, file_name="and.model", plot_name="and.png")
    except Exception as e:
        logging.exception(e)
        raise e # raise exception in terminal
    

    