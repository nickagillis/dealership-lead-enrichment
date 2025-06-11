#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    """Entry point that starts the LangGraph server"""
    # Change to the backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Start the LangGraph server
    subprocess.run([
        sys.executable, "-m", "langgraph", "dev", 
        "--host", "0.0.0.0", 
        "--port", str(os.environ.get("PORT", "8000"))
    ])

if __name__ == "__main__":
    main()
