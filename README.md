 FAQForge
# FAQForge

FAQForge is a Django web app that helps manage FAQs in different languages like English, Hindi, and Bengali. It includes a WYSIWYG editor to format answers easily, and automatically translates FAQs using Google Translate. The app uses Redis for faster performance and has a REST API to get FAQs. You can manage everything from an easy-to-use admin panel.

## Features

- Multilingual FAQs (English, Hindi, Bengali).
- WYSIWYG editor for formatting answers.
- Automatic translation with Google Translate.
- Faster performance with Redis caching.
- REST API to get FAQs.
- Simple admin panel to manage FAQs.

## How to Run the Project

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/faqforge.git
    cd faqforge
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:
    ```bash
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the server:
    ```bash
    python manage.py runserver
    ```

Now open your browser and visit `http://127.0.0.1:8000` to see the app.

## API Usage

- Get FAQs in English:
    ```bash
    curl http://localhost:8000/api/faqs/
    ```

- Get FAQs in Hindi:
    ```bash
    curl http://localhost:8000/api/faqs/?lang=hi
    ```

- Get FAQs in Bengali:
    ```bash
    curl http://localhost:8000/api/faqs/?lang=bn
    ```

## Running Tests

To run tests, use:
```bash
pytest

