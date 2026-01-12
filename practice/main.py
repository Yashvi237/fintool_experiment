"""
Personal Finance Management Tool
Main entry point for the application

This is your first Python GUI application!
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class FinanceApp:
    """Main application class for Finance Tool"""
    
    def __init__(self, root):
        """Initialize the application"""
        self.root = root
        self.root.title("Personal Finance Manager")
        self.root.geometry("800x600")
        
        # Create the main frame
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        
        # Title label
        title_label = ttk.Label(
            self.root,
            text="Welcome to Your Finance Tool!",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)
        
        # Info label
        info_label = ttk.Label(
            self.root,
            text="Your first Tkinter window with embedded matplotlib chart",
            font=("Arial", 10)
        )
        info_label.pack(pady=10)
        
        # Create a sample matplotlib chart
        self.create_sample_chart()
        
    def create_sample_chart(self):
        """Create a sample chart to test matplotlib integration"""
        
        # Sample data using numpy (like you'd use in control systems!)
        months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
        income = np.array([3000, 3200, 3100, 3300, 3400, 3500])
        expenses = np.array([2000, 2100, 1900, 2200, 2300, 2100])
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(7, 4))
        
        # Plot data
        x_pos = np.arange(len(months))
        width = 0.35
        
        ax.bar(x_pos - width/2, income, width, label='Income', color='green', alpha=0.7)
        ax.bar(x_pos + width/2, expenses, width, label='Expenses', color='red', alpha=0.7)
        
        # Customize chart
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Amount ($)', fontsize=12)
        ax.set_title('Income vs Expenses - Sample Data', fontsize=14, fontweight='bold')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(months)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Embed the chart in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)


def main():
    """Main function to run the application"""
    
    # Create the main window
    root = tk.Tk()
    
    # Create the application
    app = FinanceApp(root)
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
