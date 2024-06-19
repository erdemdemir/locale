### IMPORTS ###
import streamlit as st
import pandas as pd
import zipfile
from io import BytesIO
import docx
import re
from time import sleep

import os


### FUNCTION DEFINITIONS ###
def extract_docx_from_zip(zip_file):
    """Extracts .docx files from a zip archive and returns a list of document names and their contents."""
    docx_files = []
    valid_docx_pattern = re.compile(r"^(?!~\$)[a-zA-Z0-9].*\.docx$")
    try:
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            for file in zip_ref.namelist():
                if valid_docx_pattern.match(file) and "__MACOSX" not in file:
                    try:
                        with zip_ref.open(file) as docx_file:
                            doc = docx.Document(docx_file)
                            file_name = os.path.basename(file)
                            docx_files.append((file_name, doc))
                    except Exception as e:
                        st.warning(f"Skipping file {file}: {e}")
    except zipfile.BadZipFile:
        st.error("The uploaded file is not a valid zip file.")
    except Exception as e:
        st.error(f"An error occurred while extracting files: {e}")
    return docx_files


def extract_variables_from_docx(doc, prefix, suffix):
    """Extracts variables from a docx document based on the given prefix and suffix."""
    variables = set()
    for para in doc.paragraphs:
        text = para.text
        while prefix in text and suffix in text:
            start = text.find(prefix)
            end = text.find(suffix, start) + len(suffix)
            if start != -1 and end != -1:
                variable = text[start:end]
                variables.add(variable)
                text = text[end:]
            else:
                break
    return variables


### SESSION STATE ###

if "coord" not in st.session_state:
    st.session_state.coord = "zip"

if "docx_zip" not in st.session_state:
    st.session_state.docx_zip = None

if "variables_df" not in st.session_state:
    st.session_state.variables_df = pd.DataFrame(columns=["document_name", "variable"])

### MAIN / HEADING ###

with st.sidebar:
    if st.button("🔄 Reset 'Coordination' tool"):
        st.session_state.coord = "zip"
        st.session_state.docx_zip = None
        st.session_state.variables_df = pd.DataFrame(
            columns=["document_name", "variable"]
        )
        st.rerun()

st.title("🌐 LOCALE - Coordination")
st.caption(
    "LOcalisation of the Clinical triAls template fiLes with site-specific valuEs and site logo"
)
bosh = st.empty()

### MAIN / ZIP FILE ###

if st.session_state.coord == "zip":
    zip = bosh.container(border=True)
    with zip:
        st.markdown(
            """
You can use LOCALE to facilitate participating site localisation of the clinical trials template files. You must prepare the following in a zip package for the participating sites:

1. Template files: in docx format
2. Placeholder logo: LOCALE finds and replaces the placeholder logo in the template files and for that reason you must add a placeholder logo to all template files. See example files :red[here].
3. 'localisation.csv' file: a CSV file that includes all documents and all variables in each document. You can find more about it and download the template following this link: :red[link here]

You have 2 options to prepare the 'localisation.csv' for the sites:

1. You can use the template and examples provided in the link above to manually prepare the 'localisation.csv' file.
2. If your template files follow a pattern for variables, e.g. using chevrons to mark them as in <<Hospital name>>, <<PI name>> etc., you can use the web app below to create the 'localisation.csv' automatically to save time.
            """
        )
        uploaded_docx = st.file_uploader(
            "Upload a zip file of all docx files which will be sent to participating site for localisation",
            type="zip",
        )
        if uploaded_docx is not None and st.session_state.docx_zip is None:
            st.session_state.docx_zip = uploaded_docx.getvalue()
            st.session_state.coord = "prefix_suffix"
            bosh.empty()
            sleep(0.5)

### MAIN / PREFIX SUFFIX INPUT ###

if st.session_state.coord == "prefix_suffix":
    prefix_suffix = bosh.container(border=True)
    with prefix_suffix:
        st.header("Variable Delimiters")
        st.markdown(
            "Please provide the prefix and suffix used for variables in the document templates."
        )
        prefix = st.text_input("Prefix", value="<<")
        suffix = st.text_input("Suffix", value=">>")
        if st.button("Extract variables ➡️"):
            docx_files = extract_docx_from_zip(BytesIO(st.session_state.docx_zip))
            variables_data = []
            for doc_name, doc in docx_files:
                variables = extract_variables_from_docx(doc, prefix, suffix)
                for var in variables:
                    variables_data.append({"document_name": doc_name, "variable": var})
            st.session_state.variables_df = pd.DataFrame(variables_data)
            st.session_state.coord = "data_editor"
            bosh.empty()
            sleep(0.5)

### MAIN / DATA EDITOR ###

if st.session_state.coord == "data_editor":
    data_editor = bosh.container(border=True)
    with data_editor:
        st.header("Edit localisation.csv")
        st.markdown(
            "Please add the document type for each variable. Since the file names change with each amendment, this column will help to transfer variables from one amendment to another. To be able to transfer variables across amendments, the document type should be the same for the same document in different amendments. For example, if the document type is setup as 'GP letter' initially, it should be the same for all GP letters in different amendments. This process will be automated in the future versions."
        )
        variables_df = st.session_state.variables_df.copy()
        variables_df.insert(
            0, "document_type", ""
        )  # Insert document_type as the first column
        edited_df = st.data_editor(
            data=variables_df,
            column_config={
                "document_type": st.column_config.Column(
                    "Document type",
                    help="The type of the document",
                    width="medium",
                ),
                "document_name": st.column_config.Column(
                    "Document name",
                    help="The name of the file",
                    width="medium",
                    disabled=True,
                ),
                "variable": st.column_config.Column(
                    "Variable",
                    help="The variable to be localised",
                    width="medium",
                    disabled=True,
                ),
            },
        )
        if st.button("Save localisation.csv ⬇️"):
            edited_df.to_csv("localisation.csv", index=False)
            st.success("localisation.csv saved successfully 🎉")
            st.download_button(
                label="Download localisation.csv ⬇️",
                data=edited_df.to_csv(index=False),
                file_name="localisation.csv",
                mime="text/csv",
            )
