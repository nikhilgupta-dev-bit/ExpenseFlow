# Expense Daily

A full-stack expense tracking application built with React, Node.js, Express, and MongoDB.

## Features

- Track daily expenses
- Categorize expenses
- View expense history
- Generate expense reports
- Responsive design

## Prerequisites

- Node.js (v14 or higher)
- MongoDB
- npm or yarn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/expense-daily.git
cd expense-daily
```

2. Install server dependencies:
```bash
npm install
```

3. Install client dependencies:
```bash
cd client
npm install
```

## Environment Variables

Create a `.env` file in the root directory and add:

```
MONGODB_URI=your_mongodb_connection_string
PORT=5000
```

## Running the Application

1. Start the server (development mode):
```bash
npm run dev
```

2. Start the client:
```bash
npm run client
```

3. Or run both simultaneously:
```bash
npm run dev:full
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Project Structure

```
expense-daily/
├── client/               # React frontend
├── server/               # Express backend
│   ├── config/          # Configuration files
│   ├── controllers/     # Route controllers
│   ├── models/          # Database models
│   └── routes/          # API routes
├── .env                 # Environment variables
└── package.json         # Project dependencies
``` 