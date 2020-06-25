import matplotlib
import matplotlib.pyplot as plt 
import os
import json
import statistics


def load_dataset():
    '''
    Loads the dataset, counts images and classes
    '''
    #-- Loading the Json file as a dict
    with open('/path/to/via_export_coco.json', 'r') as f:
        label_dict = json.load(f)

    img_list = label_dict['images']
    lbl_list = label_dict['annotations']

    #-- Append the id of the annotated images to a list and count the nr of unique image id's
    img_ids = []
    for label in lbl_list:
        img_ids.append(label['image_id'])
    
    img_ids     = set(img_ids)  # Remove repeated id's
    img_ids     = list(img_ids) # Convert back to list
    image_count = len(img_ids)  # Count images in list
    print("##########################################################################################")
    print("------------------------------------------------------------------------------------------")    
    print("The dataset contains" ,image_count, "labeled images")
    print("------------------------------------------------------------------------------------------") 

    return img_ids, img_list, lbl_list

def image_stats(id_list, img_dict, lbl_dict):
    '''
    Checks the size of the labeled images in the dataset and 
    plots histogram stats of the sizes in pixels
    '''

    # Defining lists for the height and width values
    img_height = []
    img_width  = []
    img_area   = []

    for image_id in id_list:
        image_id = int(image_id)
        for img in img_dict:
            if image_id == img['id']:
                img_height.append(img['height'])
                img_width.append(img['width'])
                img_area.append(img['height']*img['width'])


    print("The mean height of the images in the set are:", statistics.mean(img_height))
    print("The mean width of the images in the set are; ", statistics.mean(img_width))
    print("------------------------------------------------------------------------------------------")

    # Histograms of the width and height of the labeled images
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    ax[0].set_title("Height")
    ax[0].hist(img_height)
    ax[1].set_title("Width")
    ax[1].hist(img_width)
    #plt.show()

    return img_area


def object_stats(id_list, img_dict, lbl_dict, img_area_list):
    '''
    Plots stats of the labeled objects in the images
    These stats include the number of objects per image
    and the percentage corverage of the objects 
    and the aspect ratio of the bounding boxes

    The annotation keys in the lbl_dict have formated
    the bounding boxes in the following way:

    lbl_dict[0]['bbox'] = [x_min, y_min, width, height]
    '''

    id_list.sort()
    object_count         = []
    object_sizes         = []
    object_aspect_ratio  = []
    
    for image_id in id_list:
        object_counter = 0
        object_area    = 0
        for annotation in lbl_dict:
            if image_id == annotation['image_id']:
                object_counter += 1
                object_area    += annotation['bbox'][2]*annotation['bbox'][3]
                object_aspect_ratio.append(annotation['bbox'][3]/annotation['bbox'][2])
        object_count.append(object_counter)
        object_sizes.append(object_area)

    print("The dataset contains a total of:", len(object_count), "labeled objects")
    print("The bounding boxes of these labeled objects covers", sum(object_sizes)/sum(img_area_list)*100,"%","of the total image area")
    print("------------------------------------------------------------------------------------------")
    print("##########################################################################################")


    # Histograms of the number of objects per image
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    ax[0].set_title("Number of corrosion ""objects"" per image")
    ax[0].hist(object_count)
    ax[1].set_title("Aspect ratio of corroded areas")
    ax[1].hist(object_aspect_ratio, bins=100, range=[0, 5])
    plt.show()





def main():
    # Dataset loader
    id_list, image_list, label_list = load_dataset() 

    # Image size stats
    img_area = image_stats(id_list, image_list, label_list)

    # Object Stats
    object_stats(id_list, image_list, label_list, img_area)


if __name__ == "__main__":
    main()
