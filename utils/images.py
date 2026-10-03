import regex as re
import os

# Takes all the image files from command line then sticks 
# them into a array that gets loop through until the array ends.

def get_images_from_html(
    html_filepath: str, resources_dir: str = "./resources"
) -> list[str]:
    """Extracts image src tags from HTML and resolves them to the /resources directory."""
    with open(html_filepath, "r", encoding="utf-8") as f:
        html = f.read()

    src_list = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)

    resolved_paths = []
    for src in src_list:
        # Keep web URLs or data URIs as-is
        if src.startswith(("http://", "https://", "data:image/")):
            resolved_paths.append(src)
        else:
            
            # Extract filename (e.g. "cat.jpg" from "assets/images/cat.jpg")
            filename = os.path.basename(src)

            # Build full path pointing directly inside /resources/
            full_path = os.path.join(resources_dir, filename)
            resolved_paths.append(full_path)

    return resolved_paths

print(get_images_from_html("./resources/cat_distribution_system_demo.html"))