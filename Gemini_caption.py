# import pathlib
# import textwrap

# import google.generativeai as genai

# import PIL.Image

# img = PIL.Image.open('images_copy/2.png')

# import os

# genai.configure(api_key=API_KEY)
# prompt ='Give me a descriptive caption for this image'
detailed_prompt = 'Based on the provided image, explain the image. If the image is a technical diagram or process etc, explain the image in technical terms in detail. if the image is a general image, describe the image in generic manner. but if the image is just plainn text, then return the text with explanaition and summary and original text with heading as \'Original Text\' and \'Summary\' and \'Explanation'
# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content([prompt,img],stream=True)

# response.resolve()
# print(response.text)

import pathlib
import textwrap
import os
from PIL import Image
import google.generativeai as genai

# Set your API key
API_KEY = ""
genai.configure(api_key=API_KEY)

# Define the prompt and detailed_prompt
prompt = 'Give me a descriptive caption for this image'
# Initialize the generative model
model = genai.GenerativeModel('gemini-pro-vision')

# Path to the images folder
images_folder = 'images_copy'

# Output markdown file
output_file_path = 'output.md'

# Iterate through each image in the folder
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for image_path in pathlib.Path(images_folder).glob('*.*'):
        # Open the image
        img = Image.open(image_path)

        # Generate content for the image
        response = model.generate_content([detailed_prompt, img], stream=True)
        response.resolve()

# Create markdown content with clickable image link
        image_link = f'![{image_path}]({image_path})'
        markdown_content = f"## {image_path}\n\n{image_link}\n\n{response.text}\n\n"

        # Write the markdown content to the output file
        output_file.write(markdown_content)

        print(f"Processed image: {image_path}")

print("Processing complete.")

