const express = require('express');
const app = express();

app.get('/api/health', (req, res) => {
  res.json({ status: 'FiBace API is running!' });
});

app.listen(3001, () => {
  console.log('FiBace API на порту 3001');
});
