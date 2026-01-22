const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("ควยไรแม็ค: ", (ans) => {
  console.log("ควยไรซ", ans);
  rl.close();
});
