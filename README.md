# Ocean Chatbot

A web-based chatbot that provides information about ocean locations, marine life, and coordinates for marine researchers, ecologists, and ocean enthusiasts.

## Features

- Get detailed information about marine animals and their habitats
- Find coordinates for specific ocean locations
- Learn about marine biodiversity and ecosystems
- User-friendly web interface

## Prerequisites

- Python 3.8+
- Google Gemini API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ocean-chatbot
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Start chatting with the ocean assistant!

## Project Structure

- `app.py` - Main Flask application
- `OceanResponse.py` - Handles AI model interactions
- `templates/` - HTML templates for the web interface
- `static/` - CSS and JavaScript files
- `.env` - Environment variables (not included in version control)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
