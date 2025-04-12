import nibabel as nib
import numpy as np
import os

dir = "128_images_unscaled"
filenames = os.listdir(dir)
for filename in filenames:
    img = nib.load(f"{dir}/{filename}")
    data = img.get_fdata()  # Get the numpy array

    # Calculate min and max
    min_val = np.min(data)
    max_val = np.max(data)

    print(f"{filename}: [{min_val}, {max_val}]")