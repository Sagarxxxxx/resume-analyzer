#!/bin/bash

echo "================================"
echo "  ResumeIQ — Setup Script"
echo "================================"

# Check Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install it from https://python.org"
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Navigate to backend
cd backend || { echo "❌ backend/ folder not found. Run this script from the project root."; exit 1; }

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "🔑 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please open backend/.env and add your Gemini API key!"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "================================"
echo "  ✅ Setup Complete!"
echo "================================"
echo ""
echo "Next steps:"
echo "  1. Add your Gemini API key to backend/.env"
echo "  2. Run the backend:  cd backend && source venv/bin/activate && uvicorn main:app --reload"
echo "  3. Open frontend/index.html in your browser"
echo ""
