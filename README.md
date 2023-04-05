                                   ==>> Flask Image Generator <==
ABOUT FLASK IMAGE GENERATOR REST Api
The Flask Image Generator is a REST API that generates solid color images with the specified width, height, color, and format parameters. It is built using the Flask web framework and the NumPy and Pillow libraries.

The API defines a single endpoint /generate_image that accepts a GET request with the following parameters:
This API can be used in a wide range of applications that require the generation of simple images with specific dimensions and color, such as testing image processing algorithms or generating placeholder images for web pages.
This is a simple Flask application that generates solid color images with the specified width, height, color, and format parameters.

Prerequisites
Before running the application, make sure you have the following prerequisites installed:

Python 3.11.3 or later
Flask
NumPy
Pillow
You can install Flask, NumPy, and Pillow using pip:
    
         pip install Flask numpy Pillow

Running the application
To run the application, open a terminal or command prompt and navigate to the directory where the main.py file is located.
Then, run the following command to start the Flask development server:

            python app.py
By default, the server will listen on http://localhost:5000/. You can access the application by opening a web browser and navigating to this URL.

Generating an image
To generate an image, make a GET request to the /generate_image endpoint with the following parameters:

*width (required): The width of the image in pixels (integer).
*height (required): The height of the image in pixels (integer).
*color (required): The color of the image (string). Allowed values are red, green, and blue.
*format (optional): The format of the image (string). Allowed values are jpeg, png, and gif. Defaults to jpeg if not specified.
For example, to generate a 200x200 green PNG image, make the following request:
         
   http://localhost:5000/generate_image?width=200&height=200&color=green&format=png

The response will be the generated image in the specified format.

Stopping the server
To stop the Flask development server, press Ctrl+C in the terminal or command prompt where the server is running.