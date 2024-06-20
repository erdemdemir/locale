html_template = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>stlite app</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.52.1/build/stlite.css" />
</head>

<body>
    <div id="root"></div>
    <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.52.1/build/stlite.js"></script>
    <script>
        stlite.mount(
            {
                requirements: ["pandas", "python-docx", "pillow", "imagehash"], // Packages to install
                entrypoint: "<<app_py>>", // The target file of the `streamlit run` command
                files: {
                    "<<app_py>>": `
<<app_py_content>>
`,
                },
            },
            document.getElementById("root")
        );
    </script>
</body>

</html>
"""

with open("streamlit/coordination.py", "r") as file:
    coordination_content = file.read()
coordination_html = html_template.replace("<<app_py>>", "Coordination.py")
coordination_html = coordination_html.replace(
    "<<app_py_content>>", coordination_content
)
with open("stlite/coordination.html", "w") as file:
    file.write(coordination_html)

with open("streamlit/site.py", "r") as file:
    site_content = file.read()
site_html = html_template.replace("<<app_py>>", "Site.py")
site_html = site_html.replace("<<app_py_content>>", site_content)
with open("stlite/site.html", "w") as file:
    file.write(site_html)

print("coordination.html and site.html has been created with the updated content.")
