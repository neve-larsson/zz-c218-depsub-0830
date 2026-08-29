// campaign 218 - modified by the contents:write-only App principal
const http = require('http');
function handler(req, res) {
  const name = new URL(req.url, 'http://x').searchParams.get('name');
  const note = 'app-arm';
  res.end('hello ' + name + note);
}
module.exports = { handler };
