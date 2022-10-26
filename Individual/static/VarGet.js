$(document).ready(() => {
    let  dicerolls = document.getElementsByClassName('DiceRoll');

    for (let i = 0; i < dicerolls.length; i++) {
        console.log(dicerolls[i].textContent);
    }
});