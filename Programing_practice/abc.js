const rows=5
for (let i = 1; i <= rows; i++) {
   let code=64
  let line = '';
  for (let j = 1; j <= rows - i; j++) {
    line += ' ';
  }
  for (let k = 1; k <= 2 * i - 1; k++) {
    code++
    line += String.fromCharCode(code)
  }
  console.log(line);
}

