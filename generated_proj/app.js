(function() {
  // Module scope variables
  const display = document.getElementById('display');
  let currentInput = '';
  let previousValue = null;
  let operator = null;

  // Helper Functions
  function updateDisplay() {
    display.textContent = currentInput || '0';
  }

  function clearAll() {
    currentInput = '';
    previousValue = null;
    operator = null;
    updateDisplay();
  }

  function backspace() {
    if (currentInput) {
      currentInput = currentInput.slice(0, -1);
      updateDisplay();
    }
  }

  function appendDigit(digit) {
    // Prevent multiple leading zeros (except when after decimal point)
    if (digit === '.' && currentInput.includes('.')) return;
    if (digit === '0' && currentInput === '0') return;
    // If starting a new number after an operator, allow leading zero
    if (currentInput === '' && digit === '.') {
      currentInput = '0.';
    } else {
      currentInput += digit;
    }
    updateDisplay();
  }

  function computePending() {
    const curr = parseFloat(currentInput);
    if (previousValue === null || isNaN(curr)) return;
    let result;
    switch (operator) {
      case '+':
        result = previousValue + curr;
        break;
      case '-':
        result = previousValue - curr;
        break;
      case '*':
        result = previousValue * curr;
        break;
      case '/':
        if (curr === 0) {
          currentInput = 'Error';
          previousValue = null;
          operator = null;
          updateDisplay();
          return;
        }
        result = previousValue / curr;
        break;
      default:
        return;
    }
    previousValue = result;
    currentInput = '';
  }

  function setOperator(op) {
    if (currentInput === '' && previousValue === null) {
      // No number entered yet; ignore operator
      return;
    }
    if (previousValue === null) {
      previousValue = parseFloat(currentInput);
    } else if (currentInput !== '') {
      computePending();
    }
    operator = op;
    currentInput = '';
    updateDisplay();
  }

  function calculate() {
    if (operator === null || currentInput === '' || previousValue === null) {
      return;
    }
    const curr = parseFloat(currentInput);
    let result;
    switch (operator) {
      case '+':
        result = previousValue + curr;
        break;
      case '-':
        result = previousValue - curr;
        break;
      case '*':
        result = previousValue * curr;
        break;
      case '/':
        if (curr === 0) {
          currentInput = 'Error';
          previousValue = null;
          operator = null;
          updateDisplay();
          return;
        }
        result = previousValue / curr;
        break;
      default:
        return;
    }
    currentInput = String(result);
    previousValue = null;
    operator = null;
    updateDisplay();
  }

  function handleButtonClick(event) {
    const btn = event.target.closest('button');
    if (!btn) return;
    const action = btn.dataset.action;
    const value = btn.dataset.value;

    switch (action) {
      case 'digit':
        appendDigit(value);
        break;
      case 'decimal':
        appendDigit('.');
        break;
      case 'operator':
        setOperator(value);
        break;
      case 'clear':
        clearAll();
        break;
      case 'backspace':
        backspace();
        break;
      case 'equals':
        calculate();
        break;
      default:
        // no-op
        break;
    }
  }

  function handleKeyboard(event) {
    const key = event.key;
    if (key >= '0' && key <= '9') {
      appendDigit(key);
    } else if (key === '.' || key === ',') {
      appendDigit('.');
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
      setOperator(key);
    } else if (key === 'Enter' || key === '=') {
      calculate();
    } else if (key === 'Escape') {
      clearAll();
    } else if (key === 'Backspace') {
      backspace();
    }
  }

  // Event Listeners
  const buttonsGrid = document.querySelector('.buttons-grid');
  if (buttonsGrid) {
    buttonsGrid.addEventListener('click', handleButtonClick);
  }
  document.addEventListener('keydown', handleKeyboard);

  // Initial display update
  updateDisplay();
})();