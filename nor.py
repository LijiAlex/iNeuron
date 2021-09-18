from utils.all_utils import createModel

def main(data, eta, epoch, file_name, plot_name):
    createModel(data, eta, epoch, file_name, plot_name)

    

if __name__ == '__main__': ##entry point
    NOR = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [1, 0, 0, 0]
    }

    ETA = 0.3 # learning rate between 0 and 1 (assume)
    EPOCHS = 10

    main(data=NOR, eta=ETA, epoch=EPOCHS, file_name="nor.model", plot_name="nor.png")