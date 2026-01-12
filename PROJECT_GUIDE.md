# Personal Finance Management Tool - Project Guide

**Last Updated**: January 11, 2026  
**Student**: Control Systems Engineer (Beginner Python, Hands-on Learner)  
**Teacher**: Full Stack Development Guide

---

## 🎯 Project Overview

Building a **desktop-based** personal finance management tool using Python with focus on data analysis and visualization.

**Architecture Decision**: Desktop Application (Windows/Cross-platform)

### Why Desktop Application?
- ✅ Perfect for learning **numpy** and **matplotlib** (core objectives!)
- ✅ Direct integration with Python scientific libraries
- ✅ Similar to engineering tools (MATLAB, LabVIEW style)
- ✅ Embedded interactive plots and data visualization
- ✅ Focus on data analysis, not web development
- ✅ Real-time chart updates and interactions

### Background Context
- **Your Experience**: Control systems engineering
- **Learning Goals**: Master numpy (numerical computing) and matplotlib (visualization)
- **Project Purpose**: Build practical tool while learning data science libraries

---

## 🛠️ Technology Stack

### Core Application
- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework (built-in, no installation needed)
- **SQLite**: Database (file-based, no separate server needed)

### Data & Visualization (PRIMARY FOCUS)
- **numpy**: Numerical computations, array operations, statistics
- **pandas**: Data manipulation and analysis (like Excel on steroids)
- **matplotlib**: 2D plotting and visualization
- **seaborn**: Statistical data visualization (built on matplotlib)

### Additional Libraries
- **sqlite3**: Database operations (built-in Python)
- **datetime**: Date/time handling (built-in)
- **ttkthemes**: Modern GUI themes (optional, for better aesthetics)

### Development Tools
- **VS Code**: Code editor (you're already using it!)
- **Git**: Version control (track changes)
- **Virtual Environment**: Isolate project dependencies
- **Jupyter Notebook**: Interactive testing of numpy/matplotlib (optional)

---

## 📚 Detailed Learning Roadmap (Hands-On, Step-by-Step)

---

### **MODULE 1: Python Fundamentals & File I/O** (Week 1-2)
**You'll Type**: Basic Python scripts to understand fundamentals

**Learning Objectives**:
- [ ] Variables, data types (strings, integers, floats, lists, dictionaries)
- [ ] Control flow (if/else, for loops, while loops)
- [ ] Functions (defining, calling, parameters, return values)
- [ ] File operations (open, read, write, close)
- [ ] Working with CSV files (reading, writing with built-in csv module)
- [ ] Error handling (try/except blocks)

**Hands-On Exercise**:
- [ ] Create a simple script to read a CSV file
- [ ] Extract specific columns from CSV
- [ ] Write filtered data to a new CSV file

**Files You'll Create**:
- `practice/basics.py` - Variable and control flow practice
- `practice/file_reader.py` - Read CSV file
- `practice/csv_writer.py` - Write data to CSV

---

### **MODULE 2: Object-Oriented Programming (OOP)** (Week 2-3)
**You'll Type**: Classes and objects for financial entities

**Learning Objectives**:
- [ ] Classes and objects (what they are and why we need them)
- [ ] `__init__` method (constructor)
- [ ] Instance variables vs class variables
- [ ] Methods (functions inside classes)
- [ ] Inheritance (creating child classes)
- [ ] Encapsulation (keeping data private)

**Hands-On Exercise**:
- [ ] Create a `Transaction` class (date, amount, description, category)
- [ ] Create a `BankStatement` class (list of transactions)
- [ ] Add methods to calculate total income/expenses

**Files You'll Create**:
- `models/transaction.py` - Transaction class
- `models/statement.py` - Statement base class
- `practice/oop_test.py` - Test your classes

---

### **MODULE 3: String Processing & Pattern Matching** (Week 3-4)
**You'll Type**: Text parsing utilities for statement processing

**Learning Objectives**:
- [ ] String methods (split, strip, replace, find)
- [ ] Regular expressions (regex) basics
- [ ] Pattern matching for extracting data
- [ ] Handling different date formats
- [ ] Currency and number parsing ($1,234.56 → 1234.56)

**Hands-On Exercise**:
- [ ] Write function to extract date from different formats
- [ ] Parse amount with currency symbols
- [ ] Extract transaction description from statement line

**Files You'll Create**:
- `utils/text_parser.py` - String parsing utilities
- `utils/date_parser.py` - Date format converter
- `practice/regex_practice.py` - Regex experiments

---

### **MODULE 4: Pandas Fundamentals** (Week 4-5)
**You'll Type**: DataFrame operations for data manipulation

**Learning Objectives**:
- [ ] Creating DataFrames from CSV, dictionaries, lists
- [ ] Selecting data (rows, columns, filtering)
- [ ] Adding/removing columns
- [ ] Sorting and grouping data
- [ ] Merging and concatenating DataFrames
- [ ] Handling missing data
- [ ] Exporting to CSV

**Hands-On Exercise**:
- [ ] Load a sample CSV into pandas DataFrame
- [ ] Filter transactions by date range
- [ ] Group by category and sum amounts
- [ ] Merge two DataFrames (like combining statements)

**Files You'll Create**:
- `practice/pandas_basics.py` - DataFrame operations
- `practice/data_merging.py` - Combine multiple CSVs
- `analytics/data_loader.py` - Load and clean data

---

### **MODULE 5: Building Your First Parser** (Week 5-6)
**You'll Type**: Checking account statement parser

**Learning Objectives**:
- [ ] Read bank statement CSV/PDF/text file
- [ ] Identify header rows vs data rows
- [ ] Extract transaction fields (date, description, amount)
- [ ] Determine transaction type (debit/credit)
- [ ] Basic categorization rules (keywords → categories)
- [ ] Save to standardized CSV format

**Hands-On Exercise**:
- [ ] Create `CheckingAccountParser` class
- [ ] Parse sample bank statement
- [ ] Categorize transactions based on keywords
- [ ] Export to `checking_transactions.csv`

**Files You'll Create**:
- `parsers/__init__.py`
- `parsers/base_parser.py` - Base parser class
- `parsers/checking_parser.py` - Checking account parser
- `data/sample_statements/checking_sample.csv` - Test data

---

### **MODULE 6: Interactive Categorization System** (Week 6-7)
**You'll Type**: User interaction and memory system

**Learning Objectives**:
- [ ] Tkinter input dialogs (askstring, messagebox)
- [ ] Creating a categorization memory database (CSV)
- [ ] Fuzzy string matching (similar descriptions)
- [ ] Loading and saving categorization rules
- [ ] Pattern-based auto-categorization

**Hands-On Exercise**:
- [ ] Create category memory CSV file
- [ ] Build function to ask user for category
- [ ] Save user's choice to memory file
- [ ] Check memory before asking again

**Files You'll Create**:
- `database/category_memory.csv` - Stores learned categories
- `utils/categorizer.py` - Categorization logic
- `gui/category_dialog.py` - Tkinter dialog for asking category

---

### **MODULE 7: Building Multiple Parsers** (Week 7-9)
**You'll Type**: Parsers for all statement types

**Learning Objectives**:
- [ ] Inheritance from base parser class
- [ ] Format-specific parsing (credit card, loans, investments)
- [ ] Handling different data layouts
- [ ] Standardizing output format across parsers

**Hands-On Exercise**:
- [ ] Create `CreditCardParser`
- [ ] Create `LoanParser`
- [ ] Create `InvestmentParser`
- [ ] Create `SalaryParser`
- [ ] Test each parser with sample data

**Files You'll Create**:
- `parsers/credit_card_parser.py`
- `parsers/loan_parser.py`
- `parsers/investment_parser.py`
- `parsers/salary_parser.py`
- Sample statement files for each type

---

### **MODULE 8: Data Consolidation** (Week 9-10)
**You'll Type**: Merge all CSVs into one central database

**Learning Objectives**:
- [ ] Reading multiple CSV files with pandas
- [ ] Standardizing column names across sources
- [ ] Concatenating DataFrames vertically
- [ ] Removing duplicate transactions
- [ ] Sorting by date
- [ ] Creating a master transactions CSV

**Hands-On Exercise**:
- [ ] Load all individual statement CSVs
- [ ] Merge into one DataFrame
- [ ] Handle duplicates and conflicts
- [ ] Export to `master_transactions.csv`

**Files You'll Create**:
- `analytics/data_consolidator.py` - Merge all data
- `data/master_transactions.csv` - Central database

---

### **MODULE 9: Numpy for Financial Calculations** (Week 10-11)
**You'll Type**: Statistical analysis with numpy

**Learning Objectives**:
- [ ] Creating numpy arrays from pandas DataFrames
- [ ] Array operations (sum, mean, median, std)
- [ ] Boolean indexing and filtering
- [ ] Calculating net worth (assets - liabilities)
- [ ] Computing investable income
- [ ] Time-based aggregations
- [ ] Moving averages and trends

**Hands-On Exercise**:
- [ ] Calculate monthly spending using numpy
- [ ] Compute category-wise totals
- [ ] Calculate 3-month moving average
- [ ] Find spending trends (increasing/decreasing)

**Files You'll Create**:
- `analytics/calculations.py` - Numpy calculations
- `analytics/statistics.py` - Statistical functions
- `analytics/net_worth.py` - Net worth calculator

---

### **MODULE 10: Matplotlib Visualizations** (Week 11-12)
**You'll Type**: Create financial charts and graphs

**Learning Objectives**:
- [ ] Creating figures and axes
- [ ] Bar charts (category spending)
- [ ] Line plots (trends over time)
- [ ] Pie charts (expense distribution)
- [ ] Subplots (multiple charts in one figure)
- [ ] Customization (colors, labels, legends, titles)
- [ ] Saving figures to files

**Hands-On Exercise**:
- [ ] Create monthly income vs expense bar chart
- [ ] Plot spending trend line chart
- [ ] Generate category breakdown pie chart
- [ ] Create multi-chart dashboard

**Files You'll Create**:
- `visualization/charts.py` - Chart creation functions
- `visualization/dashboard.py` - Multi-chart layout
- `reports/` - Folder for saved chart images

---

### **MODULE 11: GUI Integration** (Week 12-14)
**You'll Type**: Build the complete Tkinter interface

**Learning Objectives**:
- [ ] Main window layout (frames, panels)
- [ ] Menu bar (File, Tools, Reports)
- [ ] File upload dialog (select statement files)
- [ ] Progress indicators during processing
- [ ] Embedding matplotlib in Tkinter
- [ ] Displaying data in Treeview widgets
- [ ] Button event handlers

**Hands-On Exercise**:
- [ ] Create main application window
- [ ] Add file selection functionality
- [ ] Integrate parsers with GUI
- [ ] Display parsed transactions in table
- [ ] Show embedded charts

**Files You'll Create**:
- `gui/main_window.py` - Main application window
- `gui/file_selector.py` - File upload interface
- `gui/transaction_viewer.py` - Display transactions
- `gui/chart_display.py` - Embed matplotlib charts

---

### **MODULE 12: Final Integration & Polish** (Week 14-15)
**You'll Type**: Connect all modules together

**Learning Objectives**:
- [ ] Application workflow (upload → parse → categorize → consolidate → analyze)
- [ ] Error handling throughout the app
- [ ] User feedback (progress bars, status messages)
- [ ] Configuration file (settings.ini)
- [ ] Exporting reports

**Hands-On Exercise**:
- [ ] Complete end-to-end workflow
- [ ] Test with real financial statements
- [ ] Handle edge cases and errors
- [ ] Polish user experience

**Files You'll Create**:
- `main.py` - Complete application (you'll rewrite this!)
- `config/settings.ini` - Configuration file
- `utils/error_handler.py` - Error management

---

### **MODULE 13: Advanced Features (Optional)** (Week 16+)
**You'll Type**: Enhancements and predictions

**Learning Objectives**:
- [ ] Forecasting future spending (numpy polyfit)
- [ ] Budget vs actual comparison
- [ ] Alert system (overspending warnings)
- [ ] Export to PDF reports
- [ ] Goal tracking

**Files You'll Create**:
- `analytics/forecasting.py` - Prediction models
- `reports/pdf_generator.py` - PDF reports
- `utils/budget_tracker.py` - Budget monitoring

---

## 📁 Project Structure

```
Finance Tool/
│
├── PROJECT_GUIDE.md          # This file - your learning companion
├── README.md                 # Project description and setup instructions
├── requirements.txt          # Python dependencies
├── main.py                   # Application entry point (launches GUI)
│
├── database/                 # Database module
│   ├── __init__.py
│   ├── db_manager.py        # Database operations (CRUD)
│   ├── schema.sql           # Database schema definition
│   └── finance.db           # SQLite database (created automatically)
│
├── gui/                      # GUI module (Tkinter)
│   ├── __init__.py
│   ├── main_window.py       # Main application window
│   ├── transaction_form.py  # Add/edit transaction dialogs
│   ├── dashboard.py         # Dashboard with quick stats
│   └── reports_window.py    # Reports and charts view
│
├── analytics/               # Data analysis module (NUMPY/PANDAS focus)
│   ├── __init__.py
│   ├── calculations.py      # Numpy-based financial calculations
│   ├── statistics.py        # Statistical analysis functions
│   └── forecasting.py       # Trend analysis and predictions
│
├── visualization/           # Plotting module (MATPLOTLIB focus)
│   ├── __init__.py
│   ├── charts.py            # Chart generation functions
│   ├── plots.py             # Various plot types
│   └── chart_embedder.py    # Embed charts in Tkinter
│
├── models/                  # Data models
│   ├── __init__.py
│   ├── transaction.py       # Transaction class
│   ├── category.py          # Category class
│ Object-oriented programming (classes, inheritance)
- Event-driven programming (GUI callbacks)
- Error handling (try/except)
- Working with dates and times
- File I/O operations
- Module imports and project organization

### Numpy Concepts (PRIMARY FOCUS)
- **Arrays**: Creating and manipulating numpy arrays
- **Array operations**: Element-wise operations, broadcasting
- **Statistical functions**: mean, median, std, percentiles
- **Linear algebra**: Matrix operations for calculations
- **Mathematical functions**: sum, cumsum, polyfit, correlations
- **Boolean indexing**: Filter data based on conditions
- **Performance**: Why numpy is faster than Python lists

### Matplotlib Concepts (PRIMARY FOCUS)
- **Figure and Axes**: Understanding matplotlib architecture
- **Plot types**: Line, bar, scatter, pie, histogram
- **Customization**: Colors, labels, legends, titles, grids
- **Subplots**: Multiple charts in one figure
- **Embedding**: Integrate plots into Tkinter GUI
- **Interactive features**: Zoom, pan, save functionality
- **Styling**: Themes, colors, fonts

### Pandas Concepts
- **DataFrames**: 2D labeled data structures
- **Series**: 1D labeled arrays
- **Data loading**: From SQLite to DataFrame
- **Data manipulation**: Filter, sort, group, aggregate
- **Time series**: Date-based indexing and resampling
- **Export**: Save to CSV, Excel

### Tkinter GUI Concepts
- **Widgets**: Labels, Buttons, Entry, Listbox, Treeview
- **Layout managers**: Pack, Grid, Place
- **Events**: Button clicks, keyboard input
- **Frames**: Organize interface into sections
- **Dialogs**: Message boxes, file dialogs
- **Canvas**: Embed matplotlib figures

### Database Concepts (SQLite)
- **CRUD operations**: Create, Read, Update, Delete
- **SQL queries**: SELECT, INSERT, UPDATE, DELETE
- **Table design**: Primary keys, foreign keys
- **Relationships**: One-to-many relationships
- **Transactions**: Commit and rollback
- **Python integration**: sqlite3 module

### Software Engineering Practices
- **Modular design**: Separate concerns into modules
- **MVC pattern**: Model-View-Controller architecture
- **Virtual environments**: Dependency isolation
- **Version control**: Git basics
- **Code documentation**: Docstrings and comments
- **Testing**: Basic unit testingclasses
- Decorators
- List comprehensions
- Error handling (try/except)
- Working with dates and times
- File I/O operations

### Web Development Concepts
- HTTP methods (GET, POST, PUT, DELETE)
- RESTful API principles
- Templates and template inheritance
- Session management
- Form handling and validation
- Database relationships (one-to-many, many-to-many)

### Software Engineering Practices
- PrNumpy (ESSENTIAL)
- Numpy Official Documentation: https://numpy.org/doc/
- Numpy Quickstart Tutorial: https://numpy.org/doc/stable/user/quickstart.html
- Real Python Numpy Tutorial: https://realpython.com/numpy-tutorial/

### Matplotlib (ESSENTIAL)
- Matplotlinumpy, pandas, matplotlib, and other dependencies
3. Create basic project structure (folders and files)
4. Build simple Tkinter "Hello World" window
5. Test embedding a matplotlib chart in Tkinter

### Questions to Consider:
- What kind of financial data do you want to track? (bank accounts, cash, credit cards?)
- Single user application (just for you) or multi-user?
- What time period matters most? (daily, weekly, monthly, yearly?)
- Any specific charts/visualizations you want? (control engineers love good plots!)
- Do you want predictive features? (trend forecasting using numpy)python.org/3/library/tkinter.html
- Real Python Tkinter Tutorial: https://realpython.com/python-gui-tkinter/
- TkDocs Tutorial: https://tkdocs.com/tutorial/

### Database
- SQLite Python Tutorial: https://docs.python.org/3/library/sqlite3.html
- SQL Tutorial: https://www.w3schools.com/sql/

### General Python
- Python Official Tutorial: https://docs.python.org/3/tutorial/
- Real Python: https://realpython.com
- Edit existing transactions
- Delete transactions
- View transaction history

### 2. Categories
- Predefined categories (Food, Transport, Utilities, etc.)
- Custom category creation
- Category-based filtering

### 3. Dashboard
- Current balance
- This month's income/expenses
- Recent transactions
- Quick add transaction

### 4. Reports
- Monthly summary
- Category breakdown
- Income vs Expense comparison
- Visual charts

---

## 🚀 Next Steps

### Key Info Learned**: Student is control systems engineer, wants to learn numpy/matplotlib
- **Decision**: Building **desktop application** with Tkinter (revised from web app)
- **Rationale**: Better alignment with learning goals (numpy/matplotlib) and engineering background
- **Status**: Ready to start setup phase
- **Next**: Create virtual environment and install numpy, pandas, matplotlib
3. Create basic project structure
4. Run first "Hello World" Flask application
5. Test in browser (http://localhost:5000)

### Questions to Consider:
- What kind of financial data do you want to track? (bank accounts, cash, credit cards?)
- Do you need multiple user accounts, or just for yourself?
- What time period matters most? (daily, weekly, monthly, yearly?)
- Any specific features you're excited about?

---

## 📖 Resources for Learning

### Python & Flask
- Flask Official Documentation: https://flask.palletsprojects.com/
- Python Official Tutorial: https://docs.python.org/3/tutorial/
- Real Python (Flask tutorials): https://realpython.com/

### Frontend
- Bootstrap Documentation: https://getbootstrap.com/
- Chart.js Documentation: https://www.chartjs.org/
- MDN Web Docs: https://developer.mozilla.org/

### Database
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- SQL Tutorial: https://www.w3schools.com/sql/

---

## 💡 Tips for Success

1. **Start Small**: Get basic features working before adding complexity
2. **Test Frequently**: Run your app after every small change
3. **Ask Questions**: No question is too basic
4. **Break It Down**: Large tasks into smaller, manageable steps
5. **Commit Often**: Save your progress regularly
6. **Have Fun**: Enjoy the learning process!

---

## 📋 Session Notes

### Session 1 - January 11, 2026
- **Topic**: Project planning and architecture decision
- **Decision**: Building web application with Python/Flask
- **Status**: Ready to start setup phase
- **Next**: Create virtual environment and install Flask

---

## 🐛 Common Issues & Solutions

(Will be populated as we encounter and solve problems)

---

## 🎯 Milestones Achieved

- [ ] Project initialized
- [ ] First Flask app running
- [ ] Database created
- [ ] First transaction added
- [ ] Dashboard displaying data
- [ ] Charts working
- [ ] MVP complete!

---

*This document will grow with your project. Bookmark it and refer back often!*
