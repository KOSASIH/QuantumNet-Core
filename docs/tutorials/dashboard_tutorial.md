# Web Dashboard Tutorial

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Setup](#setup)
4. [Implementation](#implementation)
5. [Deployment](#deployment)
6. [Conclusion](#conclusion)
7. [Further Reading](#further-reading)

## Introduction

In this tutorial, we will build a functional web dashboard that displays real-time data using modern web technologies. The dashboard will be built using Flask for the backend, React for the frontend, and Chart.js for data visualization. By the end of this tutorial, you will have a fully functional web dashboard that you can customize and expand upon.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **React**: A JavaScript library for building user interfaces.
- **Chart.js**: A JavaScript library for creating interactive charts.
- **SQLite**: A lightweight database for storing data.
- **HTML/CSS**: For structuring and styling the web pages.

## Setup

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- Node.js and npm
- SQLite

### Step 1: Create a Virtual Environment

```bash
mkdir web_dashboard
cd web_dashboard
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 2: Install Flask

```bash
pip install Flask flask-cors
```

### Step 3: Set Up the Frontend

Create a new directory for the frontend:

```bash
npx create-react-app frontend
cd frontend
npm install chart.js react-chartjs-2 axios
```

## Implementation

### Step 4: Create the Flask Backend

Create a file named `app.py` in the `web_dashboard` directory:

```python
from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database setup
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value INTEGER)''')
    c.execute('''INSERT INTO data (value) VALUES (10), (20), (30), (40), (50)''')
    conn.commit()
    conn.close()

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### Step 5: Create the React Frontend

Navigate to the `frontend/src` directory and replace the contents of `App.js` with the following code:

```javascript
import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';

function App() {
    const [chartData, setChartData] = useState({});

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/api/data')
            .then(response => {
                const data = response.data;
                const labels = data.map(item => `Data ${item[0]}`);
                const values = data.map(item => item[1]);

                setChartData({
                    labels: labels,
                    datasets: [
                        {
                            label: 'Data Values',
                            data: values,
                            backgroundColor: 'rgba(75, 192, 192, 0.6)',
                        }
                    ]
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Web Dashboard</h1>
            <Bar data={chartData} />
        </div>
    );
}

export default App;
```

### Step 6: Run the Application

1. **Start the Flask Backend**:

   In the `web_dashboard` directory, run:

   ```bash
   python app.py
   ```

2. **Start the React Frontend**:

   In the `frontend` directory, run:

   ```bash
   npm start
   ```

### Step 7: Access the Dashboard

Open your web browser and navigate to `http://localhost:300
