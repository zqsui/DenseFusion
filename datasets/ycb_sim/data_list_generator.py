test_f = open("dataset_config/test_data_list.txt", "w")
train_f = open("dataset_config/train_data_list.txt", "w")


for j in range(1, 7):
    for i in range(0, 500):
        img_ind = 500 * (j-1) + i
        img_path = "{:04}/{:06}".format(j, img_ind)
        train_f.write(img_path + '\n')

for j in range(7, 8):
    for i in range(0, 500):
        img_ind = 500 * (j-1) + i
        img_path = "{:04}/{:06}".format(j, img_ind)
        test_f.write(img_path + '\n')