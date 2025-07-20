# Product Inventory Web App

A lightweight web application for managing products with drag-and-drop reordering and sorting capabilities.

## Features

- View products in a sortable table
- Add new products
- Reorder products using drag-and-drop
- Sort products by name or price
- Responsive design that works on desktop and mobile

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Web browser with JavaScript enabled

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd inventory_project
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

- **Adding a Product**: Fill out the form at the top of the page and click "Add Product"
- **Reordering Products**: Drag and drop rows to reorder products
- **Sorting**: Click on column headers to sort by that column (click again to reverse order)
- **Deleting a Product**: Click the "Delete" button next to the product you want to remove

## Project Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates
  - `index.html` - Main application page
- `inventory.db` - SQLite database (created automatically)
- `requirements.txt` - Python dependencies

## Technologies Used

- Backend: Python, Flask, SQLAlchemy
- Frontend: HTML5, CSS3, JavaScript, jQuery, jQuery UI
- Database: SQLite (file-based, no separate server needed)

## Deployment to Render.com

1. **Create a Render Account**
   - Go to [render.com](https://render.com/) and sign up for a free account
   - Verify your email address

2. **Deploy to Render**
   - Click the button below to deploy to Render:
     
     [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/yourusername/inventory-project)

   - Or manually:
     1. Create a new Web Service on Render
     2. Connect your GitHub repository
     3. Set the following environment variables:
        - `PYTHON_VERSION`: `3.9.0`
        - `RENDER`: `true`
     4. Click "Create Web Service"

3. **Access Your App**
   - Once deployed, you'll get a URL like `https://your-app-name.onrender.com`
   - The app might take a few minutes to start up on the free tier

## Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/inventory-project.git
   cd inventory-project
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`

## License

This project is open source and available under the [MIT License](LICENSE).
