import numpy as np
import matplotlib.pyplot as plt
import PIL 

numbers = [50]

# Generate and save the pics

for num in numbers:
    image = np.zeros((100, 100, 3))
    print(np.shape(image))
    image[:, :, 0] = 0  # Red channel
    image[:, :, 1] = 0  # Green channel
    for j in range(0,100):
        image[:, j, 2] = (np.sin(2.0 * np.pi * (j*1.0) / float(num)) + 1.0)/2.0  # Varying blue channel
        print(image[0, j, 2])
    
    im = PIL.Image.fromarray(np.uint8(image*255))
    im.save(f'w{num}_0RG.png')