const express = require('express');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS for all routes
app.use(cors());

// Middleware to parse incoming JSON
app.use(express.json());


// Endpoint to handle form submissions
app.post('/submit-form', (req, res) => {
  const formData = req.body;
  console.log('Received form data:', formData);

  // Here, you could save the data to a database or perform other actions.
  res.json({ message: 'Form data received successfully!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});