# Log File Analyzer
- Analyzes server log data and visualizes error trends

## Features
- Counts errors by type
- Counts error per day
- Generates charts using matplotlib and seaborn

## Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn

## How to Run
1. Install dependencies
   - 'pip install pandas matplotlib seaborn'
2. Place 'logs.csv' in the 'data/' folder
3. Run 'python main.py'
4. View the console and outputs. Images of the two charts will be saves in the 'images/' folder

## Dataset Details
The 'logs.csv' dataset simulates server activity with both error and non-error events

### Error Types
- 401 Unauthorized: Authentication requierd or failed
- 403 Forbidden: Server refuses to fulfill request
- 404 Not Found - Requested resource doesn't exist
- 500 Internal Server Error - Server encountered an unexpected condition
- 503 Service Unavailable - Server temporarily unavailable

### Non-Error Events
- 200 OK: Page served successfully
- User Login: User logged in successfully
- File Uploaded: File uploaded without issues
