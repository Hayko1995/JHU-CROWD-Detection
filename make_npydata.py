import os
import numpy as np


def make_npy(jhu_root):
    if not os.path.exists('./npydata'):
        os.makedirs('./npydata')
    try:
        Jhu_train_path = jhu_root + '/train/images_2048/'
        Jhu_val_path = jhu_root + '/val/images_2048/'
        jhu_test_path = jhu_root + '/test/images_2048/'

        train_list = []
        for filename in os.listdir(Jhu_train_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(Jhu_train_path + filename)
        train_list.sort()
        np.save('./npydata/jhu_train.npy', train_list)

        val_list = []
        for filename in os.listdir(Jhu_val_path):
            if filename.split('.')[1] == 'jpg':
                val_list.append(Jhu_val_path + filename)
        val_list.sort()
        np.save('./npydata/jhu_val.npy', val_list)

        test_list = []
        for filename in os.listdir(jhu_test_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(jhu_test_path + filename)
        test_list.sort()
        np.save('./npydata/jhu_test.npy', test_list)

        print("Generate JHU image list successfully")
    except:
        print("The JHU dataset path is wrong. Please check your path.")

    try:
        f = open("./data/NWPU_list/train.txt", "r")
        train_list = f.readlines()

        f = open("./data/NWPU_list/val.txt", "r")
        val_list = f.readlines()

        f = open("./data/NWPU_list/test.txt", "r")
        test_list = f.readlines()

        root = '/home/dkliang/projects/synchronous/dataset/NWPU_localization/images_2048/'
        train_img_list = []
        for i in range(len(train_list)):
            fname = train_list[i].split(' ')[0] + '.jpg'
            train_img_list.append(root + fname)
        np.save('./npydata/nwpu_train_2048.npy', train_img_list)

        val_img_list = []
        for i in range(len(val_list)):
            fname = val_list[i].split(' ')[0] + '.jpg'
            val_img_list.append(root + fname)
        np.save('./npydata/nwpu_val_2048.npy', val_img_list)

        test_img_list = []
        root = root.replace('images', 'test_data')
        for i in range(len(test_list)):
            fname = test_list[i].split(' ')[0] + '.jpg'
            fname = fname.split('\n')[0] + fname.split('\n')[1]
            test_img_list.append(root + fname)

        np.save('./npydata/nwpu_test_2048.npy', test_img_list)
        print("Generate NWPU image list successfully")
    except:
        print("The NWPU dataset path is wrong. Please check your path.")
