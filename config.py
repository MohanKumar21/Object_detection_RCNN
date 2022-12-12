import torch

BATCH_SIZE = 2 
RESIZE_TO = 256 
NUM_EPOCHS = 5 

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# training images and XML files directory
TRAIN_DIR = './train'

VALID_DIR = './test'


CLASSES = ['Atmospheric pressure limitation', 'Authorized Representative', 'Batch Code', 'Biological risks', 'Catalogue Number', 'Caution', 'Consult instructions', 'Contains Latex', 'Contains sufficient for -n- tests', 'Control', 'Date of Manufacture', 'Do not resterilize', 'Do not reuse', 'Do not use if package is damaged', 'Drops per milliliter', 'Fluid Path', 'For IVD perfomance evaluation only', 'Fragile Handle with care', 'Humidity Limitation', 'In vitro Diagnostic Medical device', 'Keep Dry', 'Keep away from sunlight', 'Liquid filter with pore size', 'Lower limit of temperature', 'Manufacturer', 'Negative Control', 'Non Pyrogenic', 'Non sterile', 'One way valve', 'Patient Number', 'Positive Control', 'Protect from heat radioactive sources', 'Sampling site', 'Sterile Fluid Path', 'Sterile', 'Sterilized using aseptic techniques', 'Sterilized using ethylene oxide', 'Sterilized using irradiation', 'Sterilized using steam', 'Temperature Limit', 'Upper limit of temperature', 'Use By Date']
NUM_CLASSES=42


VISUALIZE_TRANSFORMED_IMAGES = False

OUT_DIR = './Outputs'
SAVE_PLOTS_EPOCH = 2 
SAVE_MODEL_EPOCH = 2 