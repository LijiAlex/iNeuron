from utils.all_utils import createModel

def main(data, eta, epoch, file_name, plot_name, no_of_input):
    createModel(data, eta, epoch, file_name, plot_name, no_of_input)

    

if __name__ == '__main__': ##entry point
    NOT = {
        "x": [0,1],
        "y": [1,0]
    }

    ETA = 0.3 # learning rate between 0 and 1 (assume)
    EPOCHS = 10

    main(data=NOT, eta=ETA, epoch=EPOCHS, file_name="not.model", plot_name="not.png",no_of_input=1)