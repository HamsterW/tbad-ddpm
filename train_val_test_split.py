import os
import nibabel as nib
import random
import shutil

train_split = 0.8
val_split = 0.1

label_dir = "labels"
image_dir = "images"
filenames = os.listdir(label_dir)
has_FLT = []
no_FLT = []
for filename in filenames:
    img = nib.load(f"{label_dir}/{filename}")
    data = img.get_fdata()
    filename = filename.split("_")[0]
    if (data == 3).any():
        has_FLT.append(filename)
    else:
        no_FLT.append(filename)

random.shuffle(has_FLT)
random.shuffle(no_FLT)
FLT_size = len(has_FLT)
no_FLT_size = len(no_FLT)
print(f"No. of FLT = {FLT_size}")
print(f"No. of no FLT = {no_FLT_size}")

FLT_split_index = [(train_split) * FLT_size, (train_split + val_split) * FLT_size]
no_FLT_split_index = [(train_split) * no_FLT_size, (train_split + val_split) * no_FLT_size]

for i in range(FLT_split_index[0]):
    shutil.copy(f"{label_dir}/{has_FLT[i]}_label.nii.gz", "train_labels")
    shutil.copy(f"{image_dir}/{has_FLT[i]}_image.nii.gz", "train_images")

for i in range(FLT_split_index[0], FLT_split_index[1]):
    shutil.copy(f"{label_dir}/{has_FLT[i]}_label.nii.gz", "val_labels")
    shutil.copy(f"{image_dir}/{has_FLT[i]}_image.nii.gz", "val_images")

for i in range(FLT_split_index[1], FLT_size):
    shutil.copy(f"{label_dir}/{has_FLT[i]}_label.nii.gz", "test_labels")
    shutil.copy(f"{image_dir}/{has_FLT[i]}_image.nii.gz", "test_images")

for i in range(no_FLT_split_index[0]):
    shutil.copy(f"{label_dir}/{no_FLT[i]}_label.nii.gz", "train_labels")
    shutil.copy(f"{image_dir}/{no_FLT[i]}_image.nii.gz", "train_images")

for i in range(no_FLT_split_index[0], no_FLT_split_index[1]):
    shutil.copy(f"{label_dir}/{no_FLT[i]}_label.nii.gz", "val_labels")
    shutil.copy(f"{image_dir}/{no_FLT[i]}_image.nii.gz", "val_images")

for i in range(no_FLT_split_index[1], no_FLT_size):
    shutil.copy(f"{label_dir}/{no_FLT[i]}_label.nii.gz", "test_labels")
    shutil.copy(f"{image_dir}/{no_FLT[i]}_image.nii.gz", "test_images")