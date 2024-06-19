import streamlit as st

st.title("🌐 LOCALE - Welcome")
st.caption(
    "LOcalisation of the Clinical triAls template fiLes with site-specific valuEs and site logo - version 0.1.0"
)
st.markdown(
    """
This serverless web application aims to help coordination teams and participating sites to automate the updates needed for various templates and documents.

The current version of 🌐 LOCALE is v0.1.0. This is the first version of the application and it is still under development. You can view the code and contribute to the development of the application on [GitHub]().

**How does it work?**

**Coordination** team must create a localisation package for participating sites. This package include the following:

1. Template files: in docx format (all docx should have a placeholder logo for site's to replace)
2. Placeholder logo: The placeholder used in templates files should also be added to the zip package separately as LOCALE will use image recognition to find and replace the placeholder logo in the template files.
3. 'localisation.csv' file: a CSV file that includes all documents and all variables in each document. Since typing it manually can be error-prone and tedious, LOCALE provides a tool to generate this file from the provided Word documents. Click on the "Coordination" section on the left sidebar to view this tool.

**Participating site** then can use this zip package to update the variables in the templates, upload their site logo, and finally download the localised documents. Click on the "Site" section on the left sidebar to view this tool.

If you like to report any bugs or suggest improvements, please feel free to reach out using:

- [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSejkERce_tGQ7JJUFsxdxymT9G3tJW4g-Rl6y4GZRj2X18C-g/viewform?usp=sf_link) 
- [X (Twitter)](https://x.com/erdemdemir)
"""
)
