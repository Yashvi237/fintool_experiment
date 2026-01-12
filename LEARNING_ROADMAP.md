# 🎓 Learning Roadmap - Personal Finance Tool

**Last Updated**: January 11, 2026  
**Student**: Control Systems Engineer (Beginner Python)  
**Learning Style**: Hands-on - You will TYPE all code yourself!

---

## 🎯 Your Project Vision

Build a monthly financial health tracking tool that:

1. **Processes multiple statement types** (checking, credit card, loans, investments, salary slips)
2. **Intelligent parsing** - separate parser for each format
3. **Smart categorization** - asks you to categorize unknown transactions and remembers for next time
4. **Data consolidation** - combines all CSVs into one master file
5. **Financial insights** - net worth, spending patterns, investable income
6. **Visual analytics** - charts and graphs using matplotlib

---

## 📚 13-Module Learning Journey

Each module builds on the previous one. You'll type all code yourself to learn deeply.

---

### **MODULE 1: Python Fundamentals & File I/O** (Week 1-2)

**What You'll Learn**:
- Variables and data types (strings, int, float, lists, dictionaries)
- Control structures (if/else, for, while loops)
- Functions (def, parameters, return)
- Reading and writing files
- CSV file operations
- Error handling (try/except)

**What You'll Build**:
1. Script to read a CSV file line by line
2. Function to extract specific columns
3. Script to write filtered data to new CSV

**Practice Files You'll Create**:
```
practice/
├── basics.py          # Variables, loops, conditions
├── functions.py       # Practice writing functions  
├── file_reader.py     # Read CSV files
└── csv_writer.py      # Write to CSV files
```

**Key Concepts**:
```python
# Reading CSV example
import csv

with open('transactions.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Success Criteria**: ✅ Can read CSV, filter data, write output

---

### **MODULE 2: Object-Oriented Programming** (Week 2-3)

**What You'll Learn**:
- Classes and objects
- `__init__` constructor
- Instance variables and methods
- Class inheritance
- When and why to use OOP

**What You'll Build**:
1. `Transaction` class (date, amount, description, category)
2. `BankStatement` class that contains multiple transactions
3. Methods to calculate totals

**Files You'll Create**:
```
models/
├── __init__.py
├── transaction.py     # Transaction class
└── statement.py       # Statement base class

practice/
└── oop_test.py        # Test your classes
```

**Key Concepts**:
```python
class Transaction:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description
    
    def is_expense(self):
        return self.amount < 0
```

**Success Criteria**: ✅ Can create classes, instantiate objects, call methods

---

### **MODULE 3: String Processing & Pattern Matching** (Week 3-4)

**What You'll Learn**:
- String manipulation (split, strip, replace, find)
- Regular expressions (regex) for pattern matching
- Extracting data from text
- Parsing different date formats
- Converting currency strings to numbers

**What You'll Build**:
1. Function to parse dates ("01/15/2026", "Jan 15, 2026", "2026-01-15")
2. Function to extract dollar amounts ("$1,234.56" → 1234.56)
3. Function to clean transaction descriptions

**Files You'll Create**:
```
utils/
├── __init__.py
├── text_parser.py     # String utilities
└── date_parser.py     # Date format converter

practice/
└── regex_practice.py  # Regex experiments
```

**Key Concepts**:
```python
import re

# Extract dollar amount
text = "Purchase at Store $45.99"
match = re.search(r'\$([0-9,]+\.[0-9]{2})', text)
amount = float(match.group(1).replace(',', ''))
```

**Success Criteria**: ✅ Can parse dates, extract numbers, use regex

---

### **MODULE 4: Pandas Fundamentals** (Week 4-5)

**What You'll Learn**:
- Creating DataFrames (from CSV, dict, lists)
- Selecting rows and columns
- Filtering data (boolean indexing)
- Sorting and grouping
- Merging multiple DataFrames
- Handling missing data
- Exporting to CSV

**What You'll Build**:
1. Load CSV into DataFrame
2. Filter transactions by date range
3. Group by category and calculate totals
4. Merge two separate statement DataFrames

**Files You'll Create**:
```
practice/
├── pandas_basics.py   # DataFrame operations
└── data_merging.py    # Combine CSVs

analytics/
├── __init__.py
└── data_loader.py     # Load and clean data
```

**Key Concepts**:
```python
import pandas as pd

# Load CSV
df = pd.read_csv('transactions.csv')

# Filter
january = df[df['date'] >= '2026-01-01']

# Group and sum
by_category = df.groupby('category')['amount'].sum()
```

**Success Criteria**: ✅ Can manipulate DataFrames, filter, group, merge data

---

### **MODULE 5: Building Your First Parser** (Week 5-6)

**What You'll Learn**:
- Identifying statement formats
- Reading different file types
- Extracting transaction data
- Basic categorization (keyword matching)
- Creating standardized output

**What You'll Build**:
1. BaseParser class (parent for all parsers)
2. CheckingAccountParser class
3. Keyword-based categorization
4. Export to standardized CSV

**Files You'll Create**:
```
parsers/
├── __init__.py
├── base_parser.py         # Parent class
└── checking_parser.py     # Checking account parser

data/
└── sample_statements/
    └── checking_sample.csv
```

**Key Concepts**:
```python
class BaseParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []
    
    def parse(self):
        # Override in child classes
        raise NotImplementedError
    
    def export_to_csv(self, output_path):
        # Convert transactions to CSV
        pass
```

**Success Criteria**: ✅ Can parse checking statement and output standardized CSV

---

### **MODULE 6: Interactive Categorization System** (Week 6-7)

**What You'll Learn**:
- Tkinter dialogs (user input)
- Creating categorization memory
- Fuzzy string matching
- Loading/saving rules to CSV
- Pattern recognition

**What You'll Build**:
1. Category memory database (CSV file)
2. Function to ask user for category
3. Similarity matching for known transactions
4. Auto-categorize based on memory

**Files You'll Create**:
```
database/
├── __init__.py
└── category_memory.csv    # Learned categories

utils/
└── categorizer.py         # Categorization logic

gui/
└── category_dialog.py     # User input dialog
```

**Key Concepts**:
```python
from tkinter import simpledialog

def ask_category(description):
    category = simpledialog.askstring(
        "Unknown Transaction",
        f"Categorize: {description}\n\nCategory:"
    )
    return category
```

**Success Criteria**: ✅ Can ask user, remember choices, auto-categorize similar transactions

---

### **MODULE 7: Building Multiple Parsers** (Week 7-9)

**What You'll Learn**:
- Inheritance from BaseParser
- Handling different formats
- Credit card statements
- Loan statements
- Investment statements  
- Salary slips

**What You'll Build**:
1. CreditCardParser
2. LoanParser
3. InvestmentParser
4. SalaryParser

**Files You'll Create**:
```
parsers/
├── credit_card_parser.py
├── loan_parser.py
├── investment_parser.py
└── salary_parser.py

data/sample_statements/
├── credit_card_sample.csv
├── loan_sample.csv
├── investment_sample.csv
└── salary_sample.csv
```

**Success Criteria**: ✅ All parsers working, each exports standardized CSV

---

### **MODULE 8: Data Consolidation** (Week 9-10)

**What You'll Learn**:
- Loading multiple CSVs
- Standardizing column names
- Concatenating DataFrames
- Removing duplicates
- Date-based sorting
- Creating master database

**What You'll Build**:
1. DataConsolidator class
2. Merge all statement CSVs
3. Handle duplicate detection
4. Export to master_transactions.csv

**Files You'll Create**:
```
analytics/
└── data_consolidator.py   # Merge all CSVs

data/
└── master_transactions.csv  # Final consolidated data
```

**Key Concepts**:
```python
# Concatenate multiple DataFrames
all_dfs = [checking_df, credit_card_df, loan_df]
master_df = pd.concat(all_dfs, ignore_index=True)

# Remove duplicates
master_df = master_df.drop_duplicates()

# Sort by date
master_df = master_df.sort_values('date')
```

**Success Criteria**: ✅ All data merged into one clean CSV

---

### **MODULE 9: Numpy for Financial Calculations** (Week 10-11)

**What You'll Learn**:
- Creating numpy arrays
- Array operations (sum, mean, median, std)
- Boolean indexing
- Net worth calculations
- Investable income
- Moving averages
- Trend analysis

**What You'll Build**:
1. Net worth calculator (assets - liabilities)
2. Category-wise spending analyzer
3. Monthly trend calculator
4. 3-month moving average

**Files You'll Create**:
```
analytics/
├── calculations.py    # Core numpy calculations
├── statistics.py      # Statistical functions
└── net_worth.py       # Net worth calculator
```

**Key Concepts**:
```python
import numpy as np

# Calculate monthly spending
expenses = np.array([-500, -600, -450, -700])
total = np.sum(expenses)
average = np.mean(expenses)
std_dev = np.std(expenses)

# Moving average
window_size = 3
moving_avg = np.convolve(expenses, np.ones(window_size)/window_size, mode='valid')
```

**Success Criteria**: ✅ Can perform financial calculations using numpy arrays

---

### **MODULE 10: Matplotlib Visualizations** (Week 11-12)

**What You'll Learn**:
- Creating figures and axes
- Bar charts (category breakdown)
- Line plots (trends)
- Pie charts (distributions)
- Multiple subplots
- Customization (colors, labels, legends)
- Saving figures

**What You'll Build**:
1. Income vs Expense bar chart
2. Spending trend line plot
3. Category pie chart
4. Multi-chart dashboard

**Files You'll Create**:
```
visualization/
├── __init__.py
├── charts.py          # Chart functions
└── dashboard.py       # Multi-chart layout

reports/
└── (saved chart images)
```

**Key Concepts**:
```python
import matplotlib.pyplot as plt

# Create bar chart
categories = ['Food', 'Transport', 'Utilities']
amounts = [500, 200, 150]

fig, ax = plt.subplots()
ax.bar(categories, amounts, color='steelblue')
ax.set_title('Spending by Category')
ax.set_ylabel('Amount ($)')
plt.savefig('reports/category_chart.png')
```

**Success Criteria**: ✅ Can create multiple chart types and customize them

---

### **MODULE 11: GUI Integration** (Week 12-14)

**What You'll Learn**:
- Main window design
- Menu bars
- File selection dialogs
- Progress bars
- Embedding matplotlib in Tkinter
- Treeview for displaying data
- Event handlers

**What You'll Build**:
1. Main application window
2. File upload interface
3. Transaction display table
4. Embedded chart display
5. Complete user workflow

**Files You'll Create**:
```
gui/
├── __init__.py
├── main_window.py          # Main window
├── file_selector.py        # Upload statements
├── transaction_viewer.py   # Display table
└── chart_display.py        # Embed charts
```

**Success Criteria**: ✅ Complete GUI that connects all functionality

---

### **MODULE 12: Final Integration** (Week 14-15)

**What You'll Learn**:
- Application workflow design
- Error handling throughout
- User feedback (status messages)
- Configuration management
- Testing with real data

**What You'll Build**:
1. Complete end-to-end workflow
2. Error handling system
3. Configuration file
4. Polished user experience

**Files You'll Create**:
```
main.py                     # Rewrite complete app!
config/settings.ini         # App configuration
utils/error_handler.py      # Error management
```

**Success Criteria**: ✅ Fully functional app processing real statements

---

### **MODULE 13: Advanced Features (Optional)** (Week 16+)

**What You'll Learn**:
- Forecasting (numpy polyfit)
- Budget tracking
- PDF report generation
- Goal monitoring

**What You'll Build**:
1. Spending forecast
2. Budget vs actual
3. PDF reports

**Files You'll Create**:
```
analytics/forecasting.py
reports/pdf_generator.py
utils/budget_tracker.py
```

---

## 🎯 How We'll Work Together

### Your Role:
- **TYPE all code yourself** (I'll guide, but you write)
- Ask questions when concepts are unclear
- Test your code frequently
- Debug errors (great learning!)

### My Role:
- Explain concepts before you code
- Provide code examples to reference
- Guide you step-by-step
- Help debug when you're stuck
- Explain errors and how to fix them
- Update this roadmap as we progress

### Each Module Session:
1. **Concept Explanation** (I teach the theory)
2. **Code Example** (I show a simple example)
3. **Your Turn** (You write the code)
4. **Testing** (Run and verify it works)
5. **Debugging** (Fix any issues together)
6. **Summary** (Review what you learned)

---

## 📝 Progress Tracking

Module Completion:
- [ ] Module 1: Python Fundamentals
- [ ] Module 2: OOP
- [ ] Module 3: String Processing
- [ ] Module 4: Pandas
- [ ] Module 5: First Parser
- [ ] Module 6: Categorization
- [ ] Module 7: All Parsers
- [ ] Module 8: Consolidation
- [ ] Module 9: Numpy Analysis
- [ ] Module 10: Matplotlib
- [ ] Module 11: GUI Integration
- [ ] Module 12: Final Integration
- [ ] Module 13: Advanced Features

---

## 🚀 Next Step: Start Module 1!

Are you ready to begin Module 1 (Python Fundamentals)?

I'll explain each concept, show examples, then guide you to type the code yourself.

---

*This roadmap will be your guide throughout the journey. Reference it often!*
