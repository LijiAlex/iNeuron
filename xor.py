from utils.all_utils import createModel

def main(data, eta, epoch, file_name, plot_name):
    createModel(data, eta, epoch, file_name, plot_name)

    

if __name__ == '__main__': ##entry point
    XOR = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0, 1, 1, 0]
    }

    ETA = 0.3 # learning rate between 0 and 1 (assume)
    EPOCHS = 50

    main(data=XOR, eta=ETA, epoch=EPOCHS, file_name="xor.model", plot_name="xor.png")