const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});


//TODO: Terminar esta mierdaaa
readline.question('', x => {
  let resp = ''
  for (let index = 0; index < 9000; index++) {
    if ((String(Number(x)+1)[0] !=  String(Number(x)+1)[1]) && (String(Number(x)+1)[0] !=  String(Number(x)+1)[2]) && (String(Number(x)+1)[0] !=  String(Number(x)+1)[3])){
      if ((String(Number(x)+1)[1] !=  String(Number(x)+1)[2]) && (String(Number(x)+1)[1] !=  String(Number(x)+1)[3])) {
        if((String(Number(x)+1)[2] !=  String(Number(x)+1)[3])) {
          
          resp = String(Number(x)+1)
        }
      }
    }
    x = String(Number(x)+1)
  }

  console.log(resp)
});