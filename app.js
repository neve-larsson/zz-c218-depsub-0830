// campaign 218 - deliberately flawed OWN test code so a real alert exists to read
const http = require('http');

function handler(req, res) {
  const u = new URL(req.url, 'http://localhost');
  const expr = u.searchParams.get('expr');
  // js/code-injection - default query suite
  const result = eval(expr);
  res.end('result ' + result);
}

http.createServer(handler);
module.exports = { handler };
