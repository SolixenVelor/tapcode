# SimpleCalculator

**SimpleCalculator** is a lightweight web-based calculator that performs basic arithmetic operations. It provides an intuitive button interface, supports keyboard input, and offers responsive design for mobile devices.

---

## Tech Stack
- **HTML** – Structure of the calculator UI.
- **CSS** – Styling and responsive layout.
- **JavaScript** – Core logic for calculations, event handling, and UI updates.

---

## Features
- Basic arithmetic: addition, subtraction, multiplication, division.
- Decimal support and chaining of operations.
- Clear (C) and backspace (←) functionality.
- Keyboard shortcuts for numbers, operators, Enter (equals), Escape (clear), and Backspace.
- Real‑time display of the current expression and result.
- Error handling for division by zero and invalid input.
- Responsive layout that adapts to mobile screens.

---

## Installation / Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/simplecalculator.git
   ```
2. **Open the application**
   - Navigate to the project folder and open `index.html` in any modern web browser. No server or additional dependencies are required.

---

## Usage Guide
- **Button Layout**: The calculator UI consists of a display area at the top and a grid of buttons for digits (0‑9), decimal point, operators (`+`, `-`, `*`, `/`), equals (`=`), clear (`C`), and backspace (`←`).
- **Keyboard Shortcuts**:
  - Digits `0‑9` and `.` input the corresponding characters.
  - `+`, `-`, `*`, `/` act as the arithmetic operators.
  - `Enter` or `=` triggers calculation.
  - `Escape` clears the current expression (same as the **C** button).
  - `Backspace` deletes the last character (same as the **←** button).
- **Clear / Backspace Behavior**:
  - **Clear (C)** resets the entire expression and result.
  - **Backspace (←)** removes the last entered character, allowing quick correction.
- **Error Handling**:
  - Division by zero displays `Error` and resets the calculator.
  - Invalid sequences are ignored, and the UI prevents malformed expressions.

---

## Responsive Design
The calculator automatically adjusts its layout for smaller screens:
- Buttons stack into a compact grid.
- Font sizes scale for readability on mobile devices.
- The overall UI remains usable without horizontal scrolling.

---

## Development Notes
- **File Structure**
  - `index.html` – Markup for the calculator UI.
  - `styles.css` – Styling, including responsive media queries.
  - `app.js` – JavaScript logic handling calculations, UI updates, and event listeners.
- **Extending the Calculator**
  - To add scientific functions (e.g., sin, cos, log), create new buttons in `index.html` and implement corresponding handlers in `app.js`.
  - Update `styles.css` to accommodate any additional UI elements.
  - Ensure new functions are integrated into the expression parsing logic.

---

## License
[Insert License Here]

---

*This README provides a comprehensive overview for users and developers, ensuring easy setup, usage, and future extension of the SimpleCalculator project.*