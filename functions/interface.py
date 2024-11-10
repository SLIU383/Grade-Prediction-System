import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from functions.extract_feedbacl_process import extract_feedback_process
from functions.coreference_resolution_process import coreference_resolution_process
from functions.sentiment_analysis_process import sentiment_analysis_process
from functions.predict_grade_process import predict_grade_process
import time
import sqlite3  # Assuming grades are saved in a SQLite database

class GradePredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Prediction Application")
        self.root.geometry("800x600")  # Set a larger default window size
        self.root.resizable(False, False)  # Make the window non-resizable

        # Center Frame to hold all elements in the center of the window
        self.center_frame = tk.Frame(root)
        self.center_frame.pack(expand=True)

        # Input Folder
        self.folder_label = tk.Label(self.center_frame, text="Select Input Folder:")
        self.folder_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.folder_path_entry = tk.Entry(self.center_frame, width=50)
        self.folder_path_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
        self.folder_button = tk.Button(self.center_frame, text="Browse...", command=self.browse_folder)
        self.folder_button.grid(row=0, column=3, padx=10, pady=5)

        # Input File
        self.file_label = tk.Label(self.center_frame, text="Select Name File:")
        self.file_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.file_path_entry = tk.Entry(self.center_frame, width=50)
        self.file_path_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)
        self.file_button = tk.Button(self.center_frame, text="Browse...", command=self.browse_file)
        self.file_button.grid(row=1, column=3, padx=10, pady=5)

        # Center Start Button and View Grades Button
        self.start_button = tk.Button(self.center_frame, text="Start Process", command=self.start_process, width=20)
        self.start_button.grid(row=2, column=1, pady=20, padx=5, columnspan=2)

        self.view_grades_button = tk.Button(self.center_frame, text="View Grades", command=self.open_grades_window, width=20)
        self.view_grades_button.grid(row=3, column=1, pady=10, padx=5, columnspan=2)

        # Status Box
        self.status_text = tk.Text(self.center_frame, width=70, height=10, state="disabled")
        self.status_text.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, folder_path)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def start_process(self):
        folder_path = self.folder_path_entry.get()
        name_file_path = self.file_path_entry.get()
        
        if not folder_path or not name_file_path:
            messagebox.showwarning("Input Required", "Please select both folder and file paths.")
            return

        self.update_status("Starting process...")
        start_time = time.time()

        try:
            # Step 1: Coreference Resolution
            self.update_status("Running coreference resolution...")
            person_team_name_dic = coreference_resolution_process(folder_path, name_file_path)
            self.update_status(f"Coreference resolution finished (time spent: {time.time() - start_time:.2f} seconds)")

            # Step 2: Extract Feedback
            self.update_status("Extracting feedback...")
            extract_feedback_process(person_team_name_dic)
            self.update_status(f"Feedback extraction finished (time spent: {time.time() - start_time:.2f} seconds)")

            # Step 3: Sentiment Analysis
            self.update_status("Performing sentiment analysis...")
            sentiment_analysis_process()
            self.update_status(f"Sentiment analysis finished (time spent: {time.time() - start_time:.2f} seconds)")

            # Step 4: Predict Grade
            self.update_status("Predicting grades...")
            predict_grade_process()  # This function should save grades to the database
            self.update_status(f"Grade prediction finished (total time spent: {time.time() - start_time:.2f} seconds)")

            messagebox.showinfo("Process Complete", "All processes completed successfully.")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_status(self, message):
        self.status_text.config(state="normal")
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.config(state="disabled")
        self.status_text.yview(tk.END)  # Auto-scroll to the latest message

    def open_grades_window(self):
        # Create a new window for displaying grades
        grades_window = tk.Toplevel(self.root)
        grades_window.title("Predicted Grades")

        # Create a Treeview to display grades
        tree = ttk.Treeview(grades_window, columns=("Name", "Grade"), show="headings")
        tree.heading("Name", text="Student Name")
        tree.heading("Grade", text="Predicted Grade")
        tree.pack(fill="both", expand=True)

        # Fetch data from database and insert into the Treeview
        conn = sqlite3.connect("database/student_grade.db") 
        cursor = conn.cursor()
        cursor.execute("SELECT student_name, student_grade FROM feedback") 
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

        conn.close()