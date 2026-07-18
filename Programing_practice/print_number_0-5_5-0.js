let num=0;
let isTrue=true

const increment =()=>{
    if(isTrue){
      return  num ++
    }
 else{
     return num--
 }
}

setInterval(()=>{
    if(num===5){
        isTrue=false
    }
    if(num===0){
        isTrue=true
    }
   console.log(increment()) 
    
},1000)