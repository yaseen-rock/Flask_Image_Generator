from flask import Flask, request, Response, jsonify
from PIL import Image
import numpy as np
import io

app = Flask(__name__)


@app.route('/generate_image', methods=['GET'])
def generate_image():
    # Get parameters from the request
    width = request.args.get('width')
    height = request.args.get('height')
    color = request.args.get('color')
    format = request.args.get('format')

    # Validate the parameters
    if not width.isdigit() or not height.isdigit():
        return Response('Invalid width or height', status=400)
    if color not in ['red', 'green', 'blue']:
        return Response('Invalid color', status=400)
    if format not in ['jpeg', 'png', 'gif']:
        return Response('Invalid format', status=400)

    # Generate the image
    img_array = np.zeros((int(height), int(width), 3), dtype=np.uint8)
    if color == 'red':
        img_array[:, :, 0] = 255
    elif color == 'green':
        img_array[:, :, 1] = 255
    elif color == 'blue':
        img_array[:, :, 2] = 255

    # Convert the image array to bytes
    img = Image.fromarray(img_array)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format=format)
    img_bytes.seek(0)

    # Return the image as a response
    return Response(img_bytes.read(), mimetype='image/{}'.format(format))


if __name__ == '__main__':
    app.run(debug=True)
