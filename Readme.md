# Django Test Project

This is a test project written in Django.

## How to Test

To test this project, follow the steps below:

1. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Load fixtures:
    ```bash
    python manage.py loaddata data.json
    ```

5. Execute the command to display information from the database in the terminal:
    ```bash
    python manage.py getdata
    ```

Now you have successfully set up and tested the Django test project.
"""