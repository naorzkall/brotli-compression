import streamlit as st
import requests

# Set page config
st.set_page_config(page_title='Brotli Compressor/Decompressor', layout='wide')

# Title and description
st.title('Brotli Compressor/Decompressor')
st.markdown('Upload a file to compress or uncompress using Brotli')

# File uploader tool
uploaded_file = st.file_uploader("Upload a file", type=None)

# Select action
action = st.selectbox("Select Action", ["Compress", "Uncompress"])

def process_file(file, action):
    if file is not None:
        file_bytes = file.read()
        files = {'file': (file.name, file_bytes)}
        if action == "Compress":
            url = "http://127.0.0.1:5000/compress-file"
        else:
            url = "http://127.0.0.1:5000/uncompress-file"
        response = requests.post(url, files=files)
        if response.status_code == 200:
            result = response.json()
            if action == "Compress":
                file_url = result['compressed_file_url']
                original_size = result['original_size']
                new_size = result['compressed_size']
            else:
                file_url = result['decompressed_file_url']
                original_size = result['compressed_size']
                new_size = result['decompressed_size']
            return file_url, original_size, new_size
        else:
            st.error(f"Error: Failed to {action.lower()} the file. Check the API response.")
            return None, None, None
    else:
        st.warning("Please upload a file.")
        return None, None, None

# Process the uploaded file and show the results
if st.button('Submit'):
    if uploaded_file is not None:
        file_url, original_size, new_size = process_file(uploaded_file, action)
        if file_url:
            st.success(f"File {action.lower()}ed successfully!")
            st.write(f"Original Size: {original_size} bytes")
            st.write(f"New Size: {new_size} bytes")
    else:
        st.warning("Please upload a file.")
