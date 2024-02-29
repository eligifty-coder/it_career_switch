let i = 0
let text = ''
let continue_txt =''
// do {
//    text+="The number is "+i
//    console.log(text)
//    i++;
// }
// while (i < 10)


let cars = ["BMW", "Volvo","saab","porsche", "ferrari", 'yugo']
for (i = 0; i < cars.length; i++){
   text+= cars[i] + "<br>"
}

// const showLoop = () => {
// 	document.getElementById("demo").innerHTML = text;
// };
for (i = 0; i < 100; i++){
   if (i == 30) break;
   text+= "The number is " + i + "<br>"
}
for (i = 0; i < 10; i++){
   if (i == 6) continue;
   continue_txt += "The number is " + i + "<br>";
}
const showLoop = () => {
	document.getElementById("demo").innerHTML = continue_txt;
};