#imported modules
from astropy.io import fits
from astropy.visualization import ZScaleInterval
import matplotlib.pyplot as plt
import numpy as np
from astropy.utils.data import get_pkg_data_filename
from astropy.visualization import astropy_mpl_style
from astropy.nddata import Cutout2D
from scipy.ndimage.interpolation import rotate

z = ZScaleInterval() #assigning a module into a variable
plt.style.use(astropy_mpl_style) #making MatPlotLib use different visualization style

nircam = input("Please enter the name of the NIRCAM FITS file you want to open: " + "\n") #entering the NIRCam file name
miri = input("Please enter the name of the MIRI FITS file you want to open: " + "\n") #entering the MIRI file name

nircam_file = get_pkg_data_filename(nircam) #retrieving the data file of NIRCam
miri_file = get_pkg_data_filename(miri) #retrieving the data file of MIRI

hdulist_nircam = fits.open(nircam) #opening NIRCam FITS file
hdulist_miri = fits.open(miri) #opening MIRI FITS file

#displaying the information in an understandable style
print("\n" + "\n")
print("NIRCam")
print(hdulist_nircam.info()) #showing the Primary HDU information of NIRCam
print("\n" + "\n")
print("----------------------------------------------------------------------------------------------------------------------------")
print("\n" + "\n")
print("MIRI")
print(hdulist_miri.info()) #showing the Primary HDU information of MIRI
print("\n")

#entering the extension numbers
print("Extension numbers must be same.")
extension_nircam = int(input("Which extension image do you want to see in NIRCAM? "+"\n")) #defining the HDU extension of NIRCam
extension_miri = int(input("\n" + "Which extension image do you want to see in MIRI? "+"\n")) #defining the HDU extension of MIRI

hdu_nircam = hdulist_nircam[extension_nircam] #opening the HDU from the given extension of NIRCam
hdu_miri = hdulist_miri[extension_miri] #opening the HDU from the given extension MIRI

header_nircam = hdulist_nircam[extension_nircam].header #obtaining header of the given NIRCam extension
header_miri = hdulist_miri[extension_miri].header #obtaining header of the given MIRI extension

nircam_image_data = fits.getdata(nircam_file, ext=extension_nircam) #pulling the image data from the given NIRCam extension
miri_image_data = fits.getdata(miri_file, ext=extension_miri) #pulling the image data from the given MIRI extension

#projecting the NIRCam Image HDU
z_nir1,z_nir2 = z.get_limits(nircam_image_data) #getting the min and max values of the data
fig_nir, axes_nir = plt.subplots(nrows = 1, ncols =2) #defining subplots
axes_nir[0].imshow(nircam_image_data, vmin = z_nir1, vmax = z_nir2) #projecting image
axes_nir[1].imshow(nircam_image_data, vmin = z_nir1, vmax = z_nir2) #projecting image

#projecting the MIRI Image HDU
z_miri1, z_miri2 = z.get_limits(miri_image_data) #getting the min and max values of the data
fig_miri, axes_miri = plt.subplots(nrows = 1, ncols =2) #defining subplots
axes_miri[0].imshow(miri_image_data, vmin = z_miri1, vmax = z_miri2) #projecting image
axes_miri[1].imshow(miri_image_data, vmin = z_miri1, vmax = z_miri2) #projecting image

print("First image is NIRCam image" + "\n" + "Last image is MIRI image")

#CutOut2D initializing
x_miri_center = 1300.003016955477 #assigning the x value of center of MIRI image
y_miri_center = 589.933975818463 #assigning the y value of center of MIRI image

x_nircam_center =1900.575878822971 #assigning the x value of center of NIRCam image
y_nircam_center =1089.325394456016 #assigning the y value of center of NIRCam image

print("Your cutout NIRCam center is", "(", x_nircam_center,",", y_nircam_center, ")", "and MIRI cutout center is",
      "(", x_miri_center,",", y_miri_center, ")") #printing center values to inform the user

nircam_data = fits.getdata(nircam_file, ext = extension_nircam) #pulling data from NIRCam FITS from given extension
miri_data = fits.getdata(miri_file, ext = extension_miri) #pulling data from MIRI FITS from given extension

position_nircam = (x_nircam_center, y_nircam_center) #assigning position values of NIRCam cutout center
position_miri = (x_miri_center, y_miri_center) #assigning position values of MIRI cutout center

size_nircam = (1734,1734) #assigning the CutOut2D size for NIRCam
size_miri = (1020,1020) #assigning the CutOut2D size for MIRI

cutout_nircam = Cutout2D(nircam_data, position_nircam, size_nircam) #Cutting out the NIRCam FITS file
cutout_miri = Cutout2D(miri_data, position_miri, size_miri) #Cutting out the MIRI FITS file

print("Here is your cutout images")
print("First one is MIRI" + "\n" + "Last one is NIRCam")

#projecting the MIRI cutout image and NIRCam cutout image
z_miri1, z_miri2 = z.get_limits(miri_image_data)
fig_miri, axes_miri = plt.subplots(nrows = 1, ncols =2)
axes_miri[0].imshow(miri_image_data, vmin = z_miri1, vmax = z_miri2)
axes_miri[1].imshow(miri_image_data, vmin = z_miri1, vmax = z_miri2)

z_miri1, z_miri2 = z.get_limits(cutout_miri.data)
fig_mir, axes_mir = plt.subplots(nrows = 1, ncols =2)
axes_miri[1].imshow(cutout_miri.data, vmin = z_miri1, vmax = z_miri2)
axes_miri[0].imshow(cutout_miri.data, vmin = z_miri1, vmax = z_miri2)

z_nir1, z_nir2 = z.get_limits(cutout_nircam.data)
fig_nir, axes_nir = plt.subplots(nrows = 1, ncols =2)
axes_nir[1].imshow(cutout_nircam.data, vmin = z_nir1, vmax = z_nir2)
axes_nir[0].imshow(cutout_nircam.data, vmin = z_nir1, vmax = z_nir2)

# degrading the values of NIRCam image
# degrading NIRCam in y axis
new_nircam = [[0 for y in range(102)] for x in range(1734)]  # initializing a matrix
for k in range(1734):
    for j in range(102):
        sum_nircam = float(0)  # initializing the NIRCam sum value
        for i in range(j * 17, (j + 1) * 17):
            sum_nircam += float(cutout_nircam.data[k][i])  # summing up the values
        new_density_nircam = sum_nircam / 17  # assigning the value of new density matrix
        new_nircam[k][j] = new_density_nircam  # assigning the last version matrix to the new density matrix

new_new_nircam = [[0 for y in range(102)] for x in range(102)]  # initializing a new matrix
maxvalue_nircam = 0  # initializing the max value of NIRCam data

# degrading NIRCam in x axis
for c in range(102):
    for b in range(102):
        sum2_nircam = float(0)  # initializing the second NIRCam sum value
        for a in range(b * 17, (b + 1) * 17):
            sum2_nircam += float(new_nircam[a][c])  # summing up the values
        new_density2_nircam = sum2_nircam / 17  # assigning the value of new density matrix
        new_new_nircam[b][c] = new_density2_nircam  # assigning the last version matrix to the new density matrix

        # finding the max value of the NIRCam data densities
        if maxvalue_nircam < new_density2_nircam:
            maxvalue_nircam = new_density2_nircam

print("Max value of NIRCam image data is ", maxvalue_nircam, "\n")  # printing the max NIRCam data value

print("Here is your degraded NIRCam image with the original cutout NIRCam image")

# projecting the degraded cutout NIRCam image and original cutout NIRCam image
z_nir1, z_nir2 = z.get_limits(cutout_nircam.data)
fig_nir, axes_nir = plt.subplots(nrows=1, ncols=2)
axes_nir[1].imshow(cutout_nircam.data, vmin=z_nir1, vmax=z_nir2)
axes_nir[0].imshow(cutout_nircam.data, vmin=z_nir1, vmax=z_nir2)

z_nir1, z_nir2 = z.get_limits(new_new_nircam)
fig_nir, axes_nir = plt.subplots(nrows=1, ncols=2)
axes_nir[1].imshow(new_new_nircam, vmin=z_nir1, vmax=z_nir2)
axes_nir[0].imshow(new_new_nircam, vmin=z_nir1, vmax=z_nir2)

# degrading the values of MIRI image
# degrading MIRI in y axis
new_miri = [[0 for y in range(102)] for x in range(1020)]  # initializing a matrix
for k in range(1020):
    for j in range(102):
        sum_miri = float(0)  # initializing the MIRI sum value
        for i in range(j * 10, (j + 1) * 10):
            sum_miri += float(cutout_miri.data[k][i])  # summing up the values
        new_density_miri = sum_miri / 10  # assigning the value of new density matrix
        new_miri[k][j] = new_density_miri  # assigning the last version matrix to the new density matrix

maxvalue_miri = 0  # initializing the max value of MIRI data

new_new_miri = [[0 for y in range(102)] for x in range(102)]  # initializing a new matrix
for c in range(102):
    for b in range(102):
        sum2_miri = float(0)  # initializing the second MIRI sum value
        for a in range(b * 10, (b + 1) * 10):
            sum2_miri += float(new_miri[a][c])  # summing up the values
        new_density2_miri = sum2_miri / 10  # assigning the value of new density matrix
        new_new_miri[b][c] = new_density2_miri  # assigning the last version matrix to the new density matrix

        # finding the max value of the NIRCam data densities
        if maxvalue_miri < new_density2_miri:
            maxvalue_miri = new_density2_miri

print("Max value of MIRI image data is ", maxvalue_miri, "\n")  # printing the max value of the matrix
print("Here is your degraded MIRI image with the original cutout MIRI image")

# projecting the original cutout MIRI image and degraded cutout MIRI image
z_miri1, z_miri2 = z.get_limits(miri_image_data)
fig_miri, axes_miri = plt.subplots(nrows=1, ncols=2)
axes_miri[0].imshow(miri_image_data, vmin=z_miri1, vmax=z_miri2)
axes_miri[1].imshow(miri_image_data, vmin=z_miri1, vmax=z_miri2)

z_miri1, z_miri2 = z.get_limits(new_new_miri)
fig_mir, axes_mir = plt.subplots(nrows=1, ncols=2)
axes_miri[1].imshow(new_new_miri, vmin=z_miri1, vmax=z_miri2)
axes_miri[0].imshow(new_new_miri, vmin=z_miri1, vmax=z_miri2)

z_miri1, z_miri2 = z.get_limits(miri_image_data)
fig_miri, axes_miri = plt.subplots(nrows=1, ncols=2)
axes_miri[0].imshow(miri_image_data, vmin=z_miri1, vmax=z_miri2)
axes_miri[1].imshow(miri_image_data, vmin=z_miri1, vmax=z_miri2)

z_miri1, z_miri2 = z.get_limits(cutout_miri.data)
fig_mir, axes_mir = plt.subplots(nrows=1, ncols=2)
axes_miri[1].imshow(cutout_miri.data, vmin=z_miri1, vmax=z_miri2)
axes_miri[0].imshow(cutout_miri.data, vmin=z_miri1, vmax=z_miri2)

#normalization of MIRI and NIRCAM image
new_new_nircam2 = [[0 for y in range(102)] for x in range(102)]  #initialize a new matrix
new_new_miri2 = [[0 for y in range(102)] for x in range(102)]  #initialize a new matrix
for i in range (102):
    for j in range (102):
        new_new_miri2[i][j] = new_new_miri[i][j] / maxvalue_miri #assigning the last version matrix to the new density matrix
        new_new_nircam2[i][j] = new_new_nircam[i][j] / maxvalue_nircam #assigning the last version matrix to the new density matrix

# creating the final image
final_image = [[0 for y in range(102)] for x in range(102)]  # initialize a new matrix
for i in range(102):
    for j in range(102):
        l = new_new_miri2[i][j] / new_new_nircam2[i][j]  # dividing every value of MIRI to NIRCam values
        final_image[i][j] = l  # assigning the division result to a variable

# projecting the final image
z_final1, z_final2 = z.get_limits(final_image)
fig_final, axes_final = plt.subplots(nrows=1, ncols=2)
axes_final[0].imshow(final_image, vmin=z_final1, vmax=z_final2)
axes_final[1].imshow(final_image, vmin=z_final1, vmax=z_final2)