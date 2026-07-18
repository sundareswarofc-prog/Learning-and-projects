const input= "appletrqlatuvwxys"
let res =""
let resArr=''
let currentInput="";

for(let i=0; i<input.length;i++){
    if(!res.includes(input[i])){
        res+=input[i]
    }
    else{
    currentInput=input[i]
    if(res.length>resArr.length)
      resArr=input[i]+res
    res=""
    }
    if(i===input.length-1){
        if(res.length>resArr.length)
    resArr=currentInput+res
    }
}
console.log(resArr)