const arr=[10,2,3,4,6,20]
let resvalue=0
let temp=0;
let resArr=[]

for(let i=0;i<arr.length-2;i++){
     temp=arr[i]+arr[i+1]+arr[i+2]
     if(temp>resvalue){
         resArr=[]
         resArr.push(arr[i],arr[i+1],arr[i+2])
         resvalue=temp
     }
}

console.log(resvalue,resArr)