# Flask Brotli Compression API
This repository contains a Flask API implementation that demonstrates the use of the Brotli compression algorithm. This project was created as an extension for a university presentation on Brotli.

## Repository Contents
- `flaskapi.py`: Flask API script demonstrating Brotli compression.

## What is Brotli?
Brotli is a compression algorithm developed by Google. It is designed to provide high compression ratios and fast decompression speeds, making it well-suited for web applications where bandwidth and loading times are critical.

## Brotli History
Brotli was initially released by Google in 2015. It was developed to improve web performance by reducing the size of transmitted files, which in turn decreases load times. Brotli has since been adopted by major web browsers, including Chrome, Firefox, and Edge, as well as widely used web servers and CDNs.

## Why Use Brotli Instead of Other Compression Algorithms?
- **Higher Compression Ratios**: Brotli typically offers better compression ratios than gzip, meaning it can reduce the size of files more effectively.
- **Faster Decompression**: Despite its high compression ratio, Brotli decompression is fast, which is crucial for web performance.
- **Modern Web Standards**: Brotli is supported by modern web browsers and can be used for HTTP compression, making it a practical choice for web applications.

## How Brotli Works Behind the Scenes
Brotli uses a combination of modern compression techniques to achieve its high performance:
1. **Dictionary-Based Compression**: Brotli includes a pre-defined dictionary of common strings and phrases found in web content, which helps it achieve higher compression ratios.
2. **Huffman Coding**: Brotli uses Huffman coding, a method of entropy encoding used in lossless data compression, to represent frequently occurring characters with shorter codes.
3. **Window Sliding**: Brotli employs a window sliding mechanism to compress data by referencing previous data blocks, similar to the LZ77 algorithm.
4. **Context Modeling**: Brotli uses context modeling to make better predictions about data patterns, which enhances its compression efficiency.

## Getting Started

To get started with this project, clone the repository and install the required dependencies.

### Prerequisites
- Python 3.7+
- Flask
- Brotli

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/naorzkall/flask-brotli-compression.git
    cd flask-brotli-compression
    ```
2. Install the required dependencies:
    ```bash
    pip install Flask brotli
    ```

3. Run the Flask API:
    ```bash
    python flaskapi.py
    ```

## Usage
Once the Flask API is running, you can use it to demonstrate Brotli compression. Make requests to the endpoints provided in the `flaskapi.py` script to see Brotli in action.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Google for developing the [Brotli compression algorithm](https://github.com/google/brotli).
- The Flask community for providing the tools to build this API.
