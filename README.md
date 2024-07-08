# Acute Ai

## Overview

This application is designed for people with diabetes to link various sources of their health data, including Glucose Monitoring, Insulin Pump, and Wearables Technology. By integrating these data sources, the application provides AI-driven insights using Large Language Models (LLMs) to help manage diabetes more effectively.

## Features

- **Data Integration**: Connect and sync data from glucose monitors, insulin pumps, and wearable devices.
- **AI-Driven Insights**: Utilize advanced AI algorithms and LLMs to analyze the integrated data and provide personalized health insights.
- **User-Friendly Interface**: Easy-to-use interface to manage and view health data.
- **Secure Data Handling**: Ensures that all personal health data is securely stored and handled according to HIPAA regulations.

## Installation

### Prerequisites

- Node.js (version 14.x or higher)
- Python (version 3.8 or higher)
- MongoDB (for data storage)
- Docker (optional, for containerization)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/diabetes-data-insights.git
    cd diabetes-data-insights
    ```

2. **Install Node.js Dependencies**:
    ```bash
    npm install
    ```

3. **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add the following variables:
    ```
    MONGO_URI=your_mongo_db_uri
    NODE_ENV=development
    PORT=3000
    ```

5. **Run the Application**:
    - **Development Mode**:
        ```bash
        npm run dev
        ```
    - **Production Mode**:
        ```bash
        npm start
        ```

6. **(Optional) Using Docker**:
    ```bash
    docker-compose up --build
    ```

## Demo

Short demo video: https://www.tella.tv/video/clwpybzz1084l09kzb2z24vxd/view

