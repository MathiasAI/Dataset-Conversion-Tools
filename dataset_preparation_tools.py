import os
import shutil
import glob

# Path defines
label_path        = "/path/to/yolov3/data/labels" 
image_source      = "/path/to/image_source/"
image_destination = "/path/to/yolov3/data/images"
label_list = os.listdir(label_path)
image_list = os.listdir(image_source)



def compare_and_copy():
    '''
    This function compares the label names from the label folder
    and copies images with matching names from the dataset folder to the image folder
    '''
    # Looping through files in both folders and comparing them
    for label in label_list:
        for image in image_list:
            if image[:-4] == label[:-4]:
                shutil.copy2(image_source + image, image_destination)


def train_val_split_list():
    '''
    Splits the dataset into train/val/test sets
    by creating a list of the images belonging to each set 
    '''
    # Percentage of images to be used for the validation set
    percentage_validation = 20

    # Create train.txt and valid.txt
    file_train = open('train.txt', 'w')
    file_valid = open('valid.txt', 'w')

    # Append to train.txt and valid.txt
    counter = 1
    index_test = round(100 / percentage_validation)
    for file in glob.iglob(os.path.join(image_destination, '*.jpg')):
        title, ext = os.path.splitext(os.path.basename(file))
        if counter == index_test:
            counter = 1
            file_valid.write(image_destination + "/" + title + '.jpg' + "\n")
        else:
            file_train.write(image_destination + "/" + title + '.jpg' + "\n")
            counter = counter + 1



def main():
    #compare_and_copy()
    train_val_split_list()

if __name__ == "__main__":
    main()
