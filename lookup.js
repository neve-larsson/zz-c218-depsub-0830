// ccr trigger probe
function lookup(userInput) {
  const table = {};
  const k = String(userInput).trim();
  return table[k];
}
module.exports = { lookup };
