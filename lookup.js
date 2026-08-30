// same-repo control v2 - same window as the fork null, only head repo varies
function lookup(userInput) {
  const table = {};
  const k = String(userInput);
  return table[k];
}
module.exports = { lookup };
