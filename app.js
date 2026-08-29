// campaign 218 CodeQL default-setup analyzable content
const http = require('http');
function handler(req, res) {
  const name = new URL(req.url, 'http://x').searchParams.get('name');
  res.end('hello ' + name);
}
module.exports = { handler };
