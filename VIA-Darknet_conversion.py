import json

#-- Loading the Json file as a dict
with open('/path/to/via_export_coco.json', 'r') as f:
    label_dict = json.load(f)

img_list = label_dict['images']
lbl_list = label_dict['annotations']
current_img = 0

#-- Looping through the labels and writing the positions and sizes of bboxes to file
for label in lbl_list:

    #-- Calculating the normalized x and y positions as well as the bbox sizes
    img_id       = int(label['image_id'])
    img          = img_list[img_id]
    class_nr     = 0
    x_pos        = (label['bbox'][0]+0.5*label['bbox'][2])/img['width']
    y_pos        = (label['bbox'][1]+0.5*label['bbox'][3])/img['height']
    bbox_width   = (label['bbox'][2])/img['width']
    bbox_height  = (label['bbox'][3])/img['height']

    #-- Creating a .txt file for the labels
    file_name = img['file_name']
    file_name = file_name[:-4] # Removing .jpg
    lines_of_text = round(class_nr, 6), round(x_pos, 6), round(y_pos, 6), round(bbox_width, 6), round(bbox_height, 6) 
    lines_of_text = ' '.join(map(str, lines_of_text))

    #-- Appending the bbox position to the file belonging to current image
    if label['id'] <= len(lbl_list) - 1:
        if current_img == img_id:
            file = open(file_name + '.txt', 'a')
            file.write(lines_of_text + '\n')
        else:
            file.close
            current_img = img_id
            file = open(file_name + '.txt', 'a')
            file.write(lines_of_text + '\n')
    else:
        file.close





