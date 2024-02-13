let checkSign = ""
let checkedVal = ""
let calculatedVal = ''
let displayedVal = 0
let clearResultFromEqualFUnc = ""
let decimalVal =''
function input(e) {

   let result = document.getElementById("result")
   let periodValArr = result.value.split(" ")
   let theIndexOfPeriod = periodValArr.indexOf(".");
   let numberNextToPeriod = periodValArr[theIndexOfPeriod - 1];

   if (decimalVal) {
      console.log(decimalVal,'decimalVal')
      result.value=decimalVal
   }
   if (parseInt(result.value) === 0 && decimalVal === '') {
		result.value = Number(e.target.value);
   }
   else {
		result.value += Number(e.target.value);
	}
   if (checkSign.length >0) {
      let val =parseInt(e.target.value) + 0
      // result.value = val;
      checkSign = ''
   }
   if (checkedVal) {
      result.value = checkedVal +e.target.value;
   } 
   if (clearResultFromEqualFUnc) {
      result.value = checkedVal + e.target.value;
   } 
   calculatedVal = result.value
   checkedVal = "";
   clearResultFromEqualFUnc = ''
   
   decimalVal=''
}
function allClear() {
   result.value = 0
}

const percent = (event) => {
	checkSign = "%";
	clearResultFromEqualFUnc = "ipsum"; //this was add to clear the answer gotten from the square func when we press the period ie "." sign
	let result = document.getElementById("result");
	document.getElementById("result").value = (1 / 100) * parseFloat(result.value);
}

const square = (event) => {
   checkSign = "%";
   clearResultFromEqualFUnc = "ipsum"; //this was add to clear the answer gotten from the square func when we press the period ie "." sign 
   let result = document.getElementById("result")
   document.getElementById("result").value = Math.pow(result.value, 2)
};


function operators(digit) {
   
   digit = parseInt(digit)
   switch (digit) {
      case 1:
         result.value += " + "
         break
      
      case 2:
         result.value += " - "
         break
      
      case 3:
         result.value += " * "
         break
      
      case 4:
         result.value += " / "
         break
      
      case 5:
         result.value += " % "
         break
      case 6:
         let len = result.value.length
         let num = result.value[len - 1];
         if (clearResultFromEqualFUnc == Number(result.value)) {
            result.value = "0";
         }
         if (num.trim().length==0) {
            result.value+="0."
         } else  {
            result.value+='.'
         }
         break
   }
   checkedVal = document.getElementById("result").value;
}
const checkValIsFloat = (val) => {
   let valStr = val + ''
   let displayedVal = (valStr.length < 9) ? val:val.toFixed(7)
   console.log(valStr, result);
   return displayedVal
}
const equals = (event) => {
   let splitVal = result.value.split(' ')
   let calc = 0
   
   let firstDigit = Number(splitVal[0]);
   calc += firstDigit;
   
   while (splitVal.length > 1) {
      if (splitVal[1] == "+") {
         calc += Number(splitVal[2]);
      }else if (splitVal[1] == "-") {
         calc -= Number(splitVal[2]);
      }else if (splitVal[1] == "*") {
         calc *= Number(splitVal[2]);
      }else if (splitVal[1] == "/") {
         calc /= Number(splitVal[2]);
      }else if (splitVal[1] == "%") {
         calc %= Number(splitVal[2]);
      }
      splitVal.splice(0, 3)
      splitVal.unshift(calc)
   }
   let displayedValue = Number(calc);
   
   result.value = checkValIsFloat(displayedValue);
   clearResultFromEqualFUnc = Number(calc);
}

const plusMinus = () => {
   let result = document.getElementById("result");
   result.value = parseFloat(result.value) * -1;
}

