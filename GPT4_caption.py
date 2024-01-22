import base64
import os

import openai

api_key=""
openai.api_key = api_key

def openai_vision_response(image, prompt):
    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image}"
                        }
                    }
                ],
            }
        ],
        max_tokens=4096,
    )
    return response.choices[0].message.content

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

if __name__ == '__main__':
    prompt = "Give me a descriptive caption for this image"
    detailed_prompt = 'Based on the provided image, explain the image. If the image is a technical diagram or process etc, explain the image in technical terms in detail. if the image is a general image, describe the image in generic manner. but if the image is just plainn text, then return the text with explanaition and summary and original text with heading as \'Original Text\' and \'Summary\' and \'Explanation'
    images_folder = 'images_copy'
    output_md_filename = 'responses.md'

    with open(output_md_filename, 'w',encoding='utf-8') as md_file:
        for image in os.listdir(images_folder):
            image_path = os.path.join(images_folder, image)
            image_base64 = encode_image(image_path)
            print(f"Processing image: {image_path}")
            response = openai_vision_response(image_base64, detailed_prompt)
            md_file.write(f"## {image_path}\n\n")
            md_file.write(f"![{image_path}]({image_path})\n\n")
            md_file.write(response + "\n\n")
