const express = require('express');
const { Pool } = require('pg');

const app = express();
app.use(express.json());

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

app.get('/', async (req, res) => {
  res.send('<h2>Hệ thống Quản lý Hợp đồng - Đề 34</h2><p>Trạng thái: Hoạt động bình thường</p>');
});

app.get('/contracts', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json({ message: "Kết nối Database PostgreSQL thành công!", time: result.rows[0] });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
