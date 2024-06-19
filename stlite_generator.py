html_template = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>🌐 LOCALE</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.52.1/build/stlite.css" />
</head>

<body>
    <div id="root"></div>
    <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.52.1/build/stlite.js"></script>
    <script>
        stlite.mount(
            {
                requirements: ["pandas", "python-docx", "pillow", "imagehash"], // Packages to install
                entrypoint: "0_🏠_Home.py",
                files: {
                    "0_🏠_Home.py": `#HOME#`,
                    "pages/1_🌲_Coordination.py": `#COORDINATION#`,
                    "pages/2_🍃_Site.py": `#SITE#`,
                    "img/data_editor_icons.png": new Uint8Array([#IMG_DATA_EDITOR_ICONS#]),
                },
            },
            document.getElementById("root")
        );
    </script>
</body>

</html>
"""


def replace_placeholders(html_template, replacements):
    for placeholder, filename in replacements.items():
        with open(filename, "r") as file:
            content = file.read()
        html_template = html_template.replace(placeholder, content)
    return html_template


def read_image_as_js_array(image_path):
    with open(image_path, "rb") as image_file:
        return ",".join(str(byte) for byte in image_file.read())


replacements = {
    "#HOME#": "0_🏠_Home.py",
    "#COORDINATION#": "pages/1_🌲_Coordination.py",
    "#SITE#": "pages/2_🍃_Site.py",
}

resulting_html = replace_placeholders(html_template, replacements)

# Read the image as a JavaScript array and replace the placeholder
img_js_array = read_image_as_js_array("img/data_editor_icons.png")
resulting_html = resulting_html.replace("#IMG_DATA_EDITOR_ICONS#", img_js_array)

with open("index.html", "w") as file:
    file.write(resulting_html)

print("index.html has been created with the updated content.")
