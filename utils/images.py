import regex as re

# Takes all the image files from command line then sticks 
# them into a array that gets loop through until the array ends.

#
def get_images_from_file(filename):
    with open(filename, "rb") as f:
        html = f.read().decode("utf-8")

        return re.findall("<img[^>]+src=\"([^\"]+)\"", html)

print(get_images_from_file("./resources/cat_distribution_system_demo.html"))