#!/bin/bash

# Supply Chain AI Dashboard Startup Script

echo "🚚 Starting Supply Chain AI Use Case Dashboard..."
echo "================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

# Install requirements if needed
echo "📦 Installing/updating Python dependencies..."
pip3 install -r requirements.txt

# Start the dashboard
echo "🚀 Starting Streamlit dashboard..."
echo "📊 Dashboard will be available at: http://localhost:8501"
echo "🔄 Press Ctrl+C to stop the dashboard"
echo ""

streamlit run dashboard.py
