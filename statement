# Project Statement: Console ATM Simulation System

## 1. Problem Statement

Financial software must process transactions accurately, guard against unauthorized overdrafts, and gracefully handle malformed user input without crashing. Learning developers and computer science students frequently need practical examples of how object-oriented programming (OOP) principles and defensive programming apply to real-world domain problems like banking kiosks.

Existing simplified terminal banking demonstrations often mix state management, input/output parsing, and transaction verification into one monolithic block of procedural code. This leads to brittle programs that crash on unexpected input (such as strings entered into numerical fields) or allow invalid financial operations (such as negative deposits or unbacked withdrawals). There is a need for a clean, modular, and resilient console-based reference implementation that cleanly separates business logic from presentation while enforcing strict operational constraints.

## 2. Scope of the Project

### In-Scope

* **Single-Account Transactional Lifecycle:** Tracking an in-memory account balance from initial zero state through sequential deposits, balance inquiries, and withdrawals.

* **Model-View-Controller (MVC) Separation:** Isolating internal ledger rules (`ATM` class) from console menu navigation and user interaction (`ATMController` class).

* **Input Sanitization & Defensive Exception Handling:** Trapping invalid non-numeric inputs and raising descriptive standard exceptions (`ValueError`) for non-positive amounts or insufficient balances.

* **Continuous Terminal Workflow:** Interactive session loop allowing repeated user actions until an explicit exit command is triggered.

### Out-of-Scope (Future Enhancements)

* Multi-user authentication, PIN verification, and card emulation.

* Persistent external storage (relational databases, JSON/CSV ledgers).

* Network protocols, hardware interfacing (cash dispensers, receipt printers), and Graphical User Interfaces (GUI/Web).

* Multi-currency conversions, interest accrual, and credit/overdraft facilities.

## 3. Target Users

* **Computer Science & Software Engineering Students:** Learners studying Object-Oriented Analysis and Design (OOAD), class separation, and unit testing workflows.

* **Novice Python Developers:** Individuals looking for standard idioms for console error handling, loop management, and clean input validation.

* **Educators & Technical Assessors:** Instructors seeking an easy-to-evaluate baseline project demonstrating separation of concerns and test-driven development fundamentals.

## 4. High-Level Features

| **Feature** | **Category** | **Description** | 
| **Real-Time Balance Inquiry** | Financial Query | Fetches and formats the current account ledger balance on demand. | 
| **Defensive Deposit Engine** | Transaction | Credits funds to the ledger while explicitly rejecting zero or negative values. | 
| **Overdraft-Protected Withdrawal** | Transaction | Deducts funds after confirming sufficient account balance, preventing negative balances. | 
| **Input Validation & Crash Prevention** | Presentation / UI | Uses controlled `try-except` blocks to continuously prompt until valid numbers are supplied. | 
| **Session Control Loop** | Presentation / UI | Provides a clean, numbered console menu with gracefully handled termination. | 
