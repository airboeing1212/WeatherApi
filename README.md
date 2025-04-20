# Weather API Caching Project

This project connects to the Visual Crossing Weather API to fetch weather data for a specified location and date range. The weather data is cached using Redis for faster subsequent access. The project uses Python and employs various libraries for handling API requests, caching, and environment variables.

## Project Structure

- **main.py**: The main script that handles fetching weather data from the Visual Crossing Weather API.
- **cache.py**: A script responsible for managing the caching of the weather data using Redis.
- **requirements.txt**: Contains the necessary Python packages for this project.
- **.gitignore**: Specifies files and directories to be ignored by Git (e.g., sensitive information, virtual environments).

## Features

- Fetches weather data for a specified location and date range using the Visual Crossing Weather API.
- Caches the weather data in Redis for improved performance on subsequent requests.
- Supports the use of environment variables to store sensitive information like API keys and Redis connection strings.
- Saves the weather data as JSON and provides easy-to-read outputs.

## Installation

### Prerequisites
1. **Python 3.x**: Make sure Python 3 is installed on your system.
2. **Redis**: You'll need a Redis instance. You can use a cloud-based Redis service or install Redis locally.

### Steps
```bash
git clone <your-git-repository-url>
cd <your-repository-folder>

# Create and activate a virtual environment (if not already done)
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

# Install the dependencies from `requirements.txt`
pip install -r requirements.txt

# Set up environment variables for sensitive information such as the API key and Redis credentials.
# You can use a `.env` file for this purpose:
# API_KEY=your_api_key_here
# REDIS_HOST=your_redis_host_here
# REDIS_PORT=your_redis_port_here
# REDIS_PASSWORD=your_redis_password_here
# REDIS_USERNAME=your_redis_username_here

# Run the script
python main.py
