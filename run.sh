#!/bin/bash
#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Load .env variables
export $(grep -v '^#' .env | xargs)

# Run FastAPI server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001