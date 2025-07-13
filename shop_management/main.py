# pylint: disable=missing-docstring

import tkinter as tk
from tkinter import messagebox

from shop_gui import ShopGUI

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ShopGUI(root)
        root.mainloop()
    except tk.TclError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    except ImportError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
