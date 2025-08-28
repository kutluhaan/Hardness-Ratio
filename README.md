🔭 Hardness Ratio: Comparing Cosmic Images
📝 What's This All About?
Welcome to the Hardness Ratio project! This repository contains a Python script designed to help astronomers and data enthusiasts analyze astronomical images. Our goal is to compare two images of the same area of space, taken at different wavelengths by the MIRI and NIRCam instruments on the James Webb Space Telescope. By dividing one image's data matrix by the other, we can create a "hardness ratio" matrix and a visual projection of it. This is a crucial step in understanding the properties of celestial objects.

🚀 What Can It Do?
FITS File Handling: It can read and process FITS files, which are the standard file format for astronomical data.

Image Manipulation: It can modify and normalize images, making them ready for analysis.

Hardness Ratio Calculation: The core function of the code is to divide the data from two images to produce a hardness ratio matrix.

Visual Projection: It creates a visual representation of the hardness ratio, which makes the data much easier to interpret.

Jupyter Notebook Integration: The code is designed to be run in a Jupyter Notebook, which is perfect for step-by-step analysis and visualization.

⚙️ What's Under the Hood?
This project is built with Python and uses some powerful astronomy and data science libraries.

Python: The main programming language.

Astropy: A fundamental package for astronomy in Python, used for handling FITS files and more.

Numpy: The go-to library for all numerical and matrix operations.

Matplotlib: For creating the visualizations and plots.

Jupyter Notebook: The interactive environment where the code is meant to be run.

🛠️ How to Get Started
To get this project running on your machine, you'll need to set up a Python environment and install the required libraries.

Clone the repo:

git clone https://github.com/kutluhaan/Hardness-Ratio.git
cd Hardness-Ratio

Install the dependencies:

pip install astropy numpy matplotlib

Get your FITS files:
You'll need to obtain the FITS files you want to analyze from an archive like the MAST Archive.

Run the script:
You can run the script in a Jupyter Notebook. Open the notebook and run each cell sequentially to see the analysis unfold!

🙏 A Big Thank You!
MAST Archive: For providing all the amazing open-source data from the James Webb Space Telescope.

Astropy & Matplotlib: For creating such powerful and easy-to-use libraries that make this kind of analysis possible!
