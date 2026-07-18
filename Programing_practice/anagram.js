const word_1="silent"
const word_2="listen"
let res="";
for(let i=0;i<word_1.length;i++){
if(word_2.includes(word_1[i])){
    res=true
}
else{
   res=false
    break;
}
}
console.log(res?"anagram":"not anagram")