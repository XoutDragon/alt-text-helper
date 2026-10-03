from utils.images import get_images_from_file

TEST_FILE = "/resources/cat_distribution_system_demo.html"

#test the file to make sure if a error exist in the files themselves and not in the code.
def test_get_images_from_file():
    images = get_images_from_file(TEST_FILE)
    assert len(images) > 0, "No images found in the test file."
    for image in images:
        assert image.startswith("http") or image.startswith("/"), f"Invalid image source: {image}"

    print("All tests passed for get_images_from_file.")