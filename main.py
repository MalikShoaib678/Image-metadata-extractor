from PIL import Image
from PIL.ExifTags import TAGS
import argparse

## Simple MetadataExtractor Program...
class ImageMetadataExtractor:
    def __init__(self):
        self.metadata = {}

    def extract_metadata(self, image_file):
        image = Image.open(image_file)
        image_info = image._getexif()

        if image_info is not None:
            for tag, value in image_info.items():
                tag_name = TAGS.get(tag, tag)
                self.metadata[tag_name] = value

        return self.metadata


if __name__ == "__main__":
    # Create an instance of the ImageMetadataExtractor class.
    extractor = ImageMetadataExtractor()

    # Parse command-line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("image_file", help="Path to the image file")
    args = parser.parse_args()

    # Read and extract metadata from the image file.
    metadata = extractor.extract_metadata(args.image_file)

    # Print the extracted metadata.
    for key, value in metadata.items():
        print(f"{key}: {value}")
        
        
        
