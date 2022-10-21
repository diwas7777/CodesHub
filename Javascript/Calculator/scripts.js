const calculator = {
  displayNumber: "0",
  operator: null,
  firstNumber: null,
  waitingForSecondNumber: false,
};

function updateDisplay() {
  document.getElementById("number").innerHTML = calculator.displayNumber;
}

function clearCalculator() {
  (calculator.displayNumber = "0"),
    (calculator.operator = null),
    (calculator.firstNumber = null),
    (calculator.waitingForSecondNumber = false);
}

function inputNumber(number) {
  if (calculator.displayNumber == "0") {
    calculator.displayNumber = number;
  } else {
    calculator.displayNumber += number;
  }
}

function inverseNumber() {
  if (calculator.displayNumber === "0") {
    return;
  }
  calculator.displayNumber = calculator.displayNumber * -1;
}

function handleOperator(operator) {
  if (!calculator.waitingForSecondNumber) {
    calculator.operator = operator;
    calculator.waitingForSecondNumber = true;
    calculator.firstNumber = calculator.displayNumber;
    calculator.displayNumber = 0;
  } else {
    alert("operator sudah di tetapkan");
  }
}

function performCalculation() {
  if (calculator.firstNumber == null || calculator.operator == null) {
    alert("anda belum menetapkan operator");
    return;
  }

  let result = 0;
  if(calculator.operator === '+'){
      result = parseInt(calculator.firstNumber) + parseInt(calculator.displayNumber);
  }else{
      result = parseInt(calculator.firstNumber) - parseInt(calculator.displayNumber);
  }

  const history = {
    firstNumber: calculator.firstNumber,
    secondNumber : calculator.displayNumber,
    operator : calculator.operator,
    result : result
  }

  putHistory(history);
  calculator.displayNumber = result;
  renderHistory();
}

let buttons = document.getElementsByClassName("box");
for (let button of buttons) {
  //   console.log(button);
  button.addEventListener("click", function (event) {
    // mendapatkan elemen object yang di klik
    const target = event.target;

    if (target.classList.contains("clear")) {
      clearCalculator();
      updateDisplay();
      return;
    }

    if(target.classList.contains('negative')){
        inverseNumber();
        updateDisplay()
        return
    }

    if(target.classList.contains('equals')){
        performCalculation();
        updateDisplay();
        return;
    }

    if(target.classList.contains('operator')){
        handleOperator(target.innerText)
        return;
    }

    inputNumber(target.innerText);
    updateDisplay();
  });
}
