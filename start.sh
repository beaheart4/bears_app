#!/bin/bash
echo " Starting Chicago Bears Stats App..."
echo ""

# Check if bears.db exists
if [ ! -f "bears.db" ]; then
  echo "⚠  bears.db not found. Copy your database file to this directory."
  exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
  echo "⚠  Python 3 is required. Please install it."
  exit 1
fi

# Install Flask if needed
python3 -c "import flask" 2>/dev/null || pip3 install flask flask-cors

# Start Flask backend
echo "✓ Starting Flask backend on http://localhost:5001"
python3 backend/app.py &
FLASK_PID=$!

sleep 1

# Open frontend
echo "✓ Opening frontend in your browser..."
if command -v open &> /dev/null; then
  open frontend/index.html
elif command -v xdg-open &> /dev/null; then
  xdg-open frontend/index.html
else
  echo "  Open frontend/index.html in your browser"
fi

echo ""
echo "🏈 Bears Stats App is running!"
echo "   Backend:  http://localhost:5001/api"
echo "   Frontend: Open frontend/index.html"
echo ""
echo "Press Ctrl+C to stop."
wait $FLASK_PID
