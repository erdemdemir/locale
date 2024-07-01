# 🌐 LOCALE

*LOcalisation of the Clinical triAls template fiLes with site-specific valuEs and site logo*
*v0.1.0*

*LOCALE* is a collection of tools to help coordination teams and participating sites to automate the updates needed for various templates and documents. You can either run the `python` files in the `streamlit` folder or use the same tools in the browser running the `html` counterpart in the `stlite` folder. You can find the links below.

## Current tools

| Name of the tool | Browser-Based App                                            | View python code                                             | View step-by-step instructions                               | Example files                                                |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Coordination     | [Coordination stlite](https://erdemdemir.github.io/locale/stlite/coordination.html) | [coordination.py](https://github.com/erdemdemir/locale/blob/main/streamlit/coordination.py) | [Step by step instructions for the Coordination tool](https://github.com/erdemdemir/locale/wiki/Step-by-step-instructions-for-the-Coordination-tool) | [docx_files.zip](https://erdemdemir.github.io/locale/example_files/docx_files.zip) |
| Site             | [Site stlite](https://erdemdemir.github.io/locale/stlite/site.html) | [site.py](https://github.com/erdemdemir/locale/blob/main/streamlit/site.py) | [Step by step instructions for the Site tool](https://github.com/erdemdemir/locale/wiki/Step-by-step-instructions-for-the-Site-tool) | [site_example_files.zip](https://erdemdemir.github.io/locale/example_files/site_example_files.zip) |

## How does it work?

**Coordination** team must create a localisation package for participating sites. This package include the following:

1. Template files: in docx format (all docx should have a placeholder logo for site's to replace)
2. Placeholder logo: The placeholder used in templates files should also be added to the zip package separately as *LOCALE* will use image recognition to find and replace the placeholder logo in the template files.
3. 'localisation.csv' file: a CSV file that includes all documents and all variables in each document. Since typing it manually can be error-prone and tedious, *LOCALE* provides "Coordination tool" to generate this file from the provided Word documents.

**Participating site** then can use this zip package to update the variables in the templates, upload their site logo, and finally download the localised documents.

If you like to report any bugs or suggest improvements, please feel free to reach out using:

- [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSejkERce_tGQ7JJUFsxdxymT9G3tJW4g-Rl6y4GZRj2X18C-g/viewform?usp=sf_link) 
- [X (Twitter)](https://x.com/erdemdemir)