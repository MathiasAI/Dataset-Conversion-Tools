# Dataset Conversion Tools
This repository contains a script to convert labels from MS COCO to Darknet format. Additional scripts to prepare and evaluate the dataset before training is also provided.

## Usage

### dataset_evaluation_tools.py
Run the script in order to inspect the validity and class balance of the labeled dataset 

Specify the path to the exported labels on line 13

    with open('/path/to/via_export_coco.json', 'r') as f:
The script plots stats of the labeled objects in the images, such as the number of objects per image and the percentage coverage of the objects and the aspect ratio of the bounding boxes. 
![enter image description here](https://qs7j8q.db.files.1drv.com/y4mmUaYh78uvKpbmhKBSDqCZIDxGYiNNBwGHhYDL7-JSdQ_Szkf8K6sNIgQYG3XdtFh12z4Zz2WkGVXriui7zhXuEzNqetBsUrRKj79LLMb7yzd32wo5ghlg2AkiIPNMR0e0PFiOiH6c67rOX4TyiAaGsmrkSJkr4tvqCKt8_OA1plY6DAPoV_63tZk3MSbTroDYuQXsYPaiaBQbLnP39iheA?width=993&height=368&cropmode=none)
![enter image description here](https://qs7i8q.db.files.1drv.com/y4m_o9EECTh0FwA1Rzce5vGSNClS6PHURKnvA2VSgXd9UG7KpTT1N5rfDzwKt8RLYW8Xg4pGvt3UoxI_eapF6bq1cNUClD6gMmNkFEEX_YK2yn3VY3bHOQ2gjQuazYutoGtRmPHPp3PFsn3tJJY60s-4EzEA_1rQHkqoNxp6PMLBqU99K7VTLNT8ANI29LlR-8lgT4lRJ5Kyjoqc9xEmu1THA?width=982&height=372&cropmode=none)

 

### VIA_Darknet_conversion.py
Run the script with the right path to the labels specified on line 4 in the script

    with open('/path/to/via_export_coco.json', 'r') as f:

The scripts converts the labels from MS COCO to Darknet format, which means, one row per object. Each row contains class number, normalized x-center, y-center, width, and height

### dataset_preparation_tools.py
Dataset_preparation_tools.py extracts images related to the converted labels and sorts them as expected by the YoloV3 implementation provided by[ Ultralytics](https://github.com/ultralytics/yolov3). The script also creates a list of images belonging to the training and validation set.

Change the paths and percentage train-val split before use.

