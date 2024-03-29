const prompt = require("prompt-sync")();

const deposit = () => {
    while(true){
        const depositAmount = prompt("Enter a deposit amount: ");
        const numberDepositAmount = parseFloat(depositAmount);

        if(isNaN(depositAmount) || numberDepositAmount <= 0){
            console.log("Invalid deposit amount, try again!");
        }
        else{
            return numberDepositAmount;
        }
    }  
}

const getNumberOfLines = () => {
    while(true){
        const lines = prompt("Enter the number of lines to bet on (1 -> 3): ");
        const numberOfLines = parseFloat(lines);

        if(isNaN(depositAmount) || numberOfLines < 1 || numberOfLines > 3){
            console.log("Invalid number of lines, try again!");
        }
        else{
            return numberOfLines;
        }
    }  
}

let balance = deposit();
const numberOfLines = getNumberOfLines();