test_f = open("dataset_config/test_data_list.txt", "w")
train_f = open("dataset_config/train_data_list.txt", "w")


for j in range(1, 48):
    if j == 2 or j == 6 or j == 37:
        continue
    for i in range(1, 501):
        #img_ind = 500 * (j-1) + i
        img_path = "data/{:04}/{:06}".format(j, i)
        train_f.write(img_path + '\n')

for j in range(2, 3):
    for i in range(1, 450):
        #img_ind = 500 * (j-1) + i
        img_path = "data/{:04}/{:06}".format(j, i)
        test_f.write(img_path + '\n')

for j in range(6, 7):
    for i in range(1, 300):
        #img_ind = 500 * (j-1) + i
        img_path = "data/{:04}/{:06}".format(j, i)
        test_f.write(img_path + '\n')

for j in range(37, 38):
    for i in range(1, 220):
        #img_ind = 500 * (j-1) + i
        img_path = "data/{:04}/{:06}".format(j, i)
        test_f.write(img_path + '\n')