# pylint: disable=missing-docstring


import tkinter as tk
from tkinter import messagebox, ttk

from shop import Shop


class ShopGUI:
    def __init__(self, main_window):
        self.shop = Shop()
        self.main_window = main_window
        self.main_window.title("BizTrack")
        self.main_window.geometry("800x600")
        self.main_window.configure(background="#2c3e50")

        # Create a style
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "TButton",
            foreground="white",
            background="#1abc9c",
            font=("Fira Code", 14, "bold"),
            padding=10,
            relief="flat",
        )

        self.style.configure(
            "TLabel",
            padding=(10, 10),
            foreground="white",
            background="#34495e",
            width=30,
        )

        self.style.configure(
            "TEntry",
            font=("Fira Code", 14, "normal"),
            padding=5,
            foreground="#2c3e50",
            background="white",
            fieldbackground="#ecf0f1",
            takefocus=True,
            cursor="hand2",
        )

        # Create a Notebook (Tabbed interface)
        self.notebook = ttk.Notebook(main_window)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Dashboard Tab
        self.dashboard_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.dashboard_frame, text="Dashboard")
        self.setup_dashboard()

        # Add Item Tab
        self.add_item_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.add_item_frame, text="Add Item")
        self.setup_add_item()

        # Sell Item Tab
        self.sell_item_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.sell_item_frame, text="Sell Item")
        self.setup_sell_item()

        # View Inventory Tab
        self.view_inventory_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(self.view_inventory_frame, text="View Inventory")
        self.setup_view_inventory()

        # View Sales Report Tab
        self.view_sales_report_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(
            self.view_sales_report_frame, text="View Sales Report"
        )
        self.setup_view_sales_report()

    def setup_header(
        self, frame, title="BizTrack Inventory Management System"
    ):
        header_label = ttk.Label(
            frame,
            text=title,
            font=("Fira Code", 24, "bold"),
            justify="center",
            width="full",
            style="TLabel",
        )
        header_label.pack(pady=20)

    def setup_dashboard(self):
        pass

    def setup_add_item(self):
        self.setup_header(self.add_item_frame, "Add Item")
        ttk.Label(
            self.add_item_frame, text="Product Name:", style="TLabel"
        ).pack(pady=5, fill=tk.X)
        self.add_product_name_entry = ttk.Entry(
            self.add_item_frame, width=30, style="TEntry"
        )
        self.add_product_name_entry.pack(pady=5, fill=tk.X)

        ttk.Label(self.add_item_frame, text="Price:", style="TLabel").pack(
            pady=5, fill=tk.X
        )
        self.add_price_entry = ttk.Entry(
            self.add_item_frame, width=30, style="TEntry"
        )
        self.add_price_entry.pack(pady=5, fill=tk.X)

        ttk.Label(self.add_item_frame, text="Quantity:", style="TLabel").pack(
            pady=5, fill=tk.X
        )
        self.add_quantity_entry = ttk.Entry(
            self.add_item_frame, width=30, style="TEntry"
        )
        self.add_quantity_entry.pack(pady=5, fill=tk.X)

        ttk.Button(
            self.add_item_frame,
            text="Add Item",
            command=self.add_item,
            style="TButton",
        ).pack(pady=20, fill=tk.X)

    def setup_sell_item(self):
        self.setup_header(self.sell_item_frame, "Sell Item")
        ttk.Label(
            self.sell_item_frame, text="Product Name:", style="TLabel"
        ).pack(pady=5, fill=tk.X)
        self.sell_product_name_entry = ttk.Entry(
            self.sell_item_frame, width=30, style="TEntry"
        )
        self.sell_product_name_entry.pack(pady=5, fill=tk.X)

        ttk.Label(self.sell_item_frame, text="Quantity:", style="TLabel").pack(
            pady=5, fill=tk.X
        )
        self.sell_quantity_entry = ttk.Entry(
            self.sell_item_frame, width=30, style="TEntry"
        )
        self.sell_quantity_entry.pack(pady=5, fill=tk.X)

        ttk.Button(
            self.sell_item_frame,
            text="Sell Item",
            command=self.sell_item,
            style="TButton",
        ).pack(pady=20, fill=tk.X)

    def setup_view_inventory(self):
        self.setup_header(self.view_inventory_frame, "View Inventory")
        self.inventory_table = ttk.Treeview(
            self.view_inventory_frame,
            columns=("Name", "Price", "Quantity"),
            show="headings",
            selectmode="extended",
        )
        self.inventory_table.heading("Name", text="Name")
        self.inventory_table.heading("Price", text="Price")
        self.inventory_table.heading("Quantity", text="Quantity")

        self.inventory_table.column("Name", anchor="center")
        self.inventory_table.column("Price", anchor="center")
        self.inventory_table.column("Quantity", anchor="center")

        self.inventory_table.pack(pady=20, fill=tk.BOTH, expand=True)

        ttk.Button(
            self.view_inventory_frame,
            text="Refresh Inventory",
            command=self.display_inventory,
            style="TButton",
        ).pack(pady=10, fill=tk.X)

    def setup_view_sales_report(self):
        self.setup_header(self.view_sales_report_frame, "View Sales Report")
        self.sales_report_table = ttk.Treeview(
            self.view_sales_report_frame,
            columns=("Name", "Quantity", "Total Price", "Sales Date"),
            show="headings",
            selectmode="extended",
        )
        self.sales_report_table.heading("Name", text="Name")
        self.sales_report_table.heading("Quantity", text="Quantity")
        self.sales_report_table.heading("Total Price", text="Total Price")
        self.sales_report_table.heading("Sales Date", text="Sales Date")

        self.sales_report_table.column("Name", anchor="center")
        self.sales_report_table.column("Quantity", anchor="center")
        self.sales_report_table.column("Total Price", anchor="center")
        self.sales_report_table.column("Sales Date", anchor="center")

        self.sales_report_table.pack(pady=20, fill=tk.BOTH, expand=True)

        ttk.Button(
            self.view_sales_report_frame,
            text="Refresh Sales Report",
            command=self.view_sales_report,
            style="TButton",
        ).pack(pady=10, fill=tk.X)

    def add_item(self):
        name = self.add_product_name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Product name cannot be empty.")
            return

        try:
            price = float(self.add_price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid price.")
            return

        try:
            quantity = int(self.add_quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantity.")
            return

        if name and quantity > 0 and price > 0:
            self.shop.add_item_to_inventory(name, price, quantity)
            messagebox.showinfo("Success", "Item added to inventory")
            self.add_product_name_entry.delete(0, tk.END)
            self.add_price_entry.delete(0, tk.END)
            self.add_quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Error", "Please enter valid item name and quantity."
            )

    def sell_item(self):
        product_name = self.sell_product_name_entry.get()
        if not product_name:
            messagebox.showerror("Error", "Product name cannot be empty.")
            return

        try:
            quantity = int(self.sell_quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantity.")
            return

        if product_name and quantity > 0:
            self.shop.sell_item(product_name, quantity)
            messagebox.showinfo("Success", "Item sold successfully.")
            self.sell_product_name_entry.delete(0, tk.END)
            self.sell_quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Error", "Please enter valid product name and quantity."
            )

    def view_sales_report(self):
        sales = self.shop.view_sales_report()

        if sales:
            try:
                self.sales_report_table.delete(
                    *self.sales_report_table.get_children()
                )
                for row in sales:
                    formatted_row = (row[1], row[2], f"${row[3]:.2f}", row[4])
                    self.sales_report_table.insert(
                        "", tk.END, values=formatted_row
                    )
            except IndexError as e:
                print(f"Error accessing sales data: {e}")
                messagebox.showerror(
                    "Error", "Sales data is not in the expected format."
                )
        else:
            self.sales_report_table.delete(
                *self.sales_report_table.get_children()
            )
            messagebox.showinfo("Info", "No sales have been made.")

    def display_inventory(self):
        inventory = self.shop.display_inventory()

        if inventory:
            try:
                self.inventory_table.delete(
                    *self.inventory_table.get_children()
                )
                for row in inventory:
                    formatted_row = (row[1], f"${row[2]:.2f}", row[3])
                    self.inventory_table.insert(
                        "", tk.END, values=formatted_row
                    )
            except IndexError as e:
                print(f"Error accessing inventory data: {e}")
                messagebox.showerror(
                    "Error", "Inventory data is not in the expected format."
                )
        else:
            self.inventory_table.delete(*self.inventory_table.get_children())
            messagebox.showinfo("Info", "Inventory is empty.")
