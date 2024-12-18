# Metropolitan Detective Agency Case Archive Management System

## Overview
This project is a Python-based application for managing an archive of criminal cases from a fictional Metropolitan Detective Agency (MDA). The application allows you to:
- Load cases from a CSV file or demo data.
- Search cases by suspect name, victim name, or case ID.
- Filter cases based on crime type, severity, or status.
- Sort cases by different attributes (case ID, date, severity, status).

The system demonstrates the use of object-oriented programming, modular design, and key algorithmic concepts like merge sort and binary search in Python 3.

## Features
- **Object-Oriented Design:** Classes `Person`, `Suspect`, `Victim`, and `Case` represent the data model. 
- **Data Loading:** Load cases from a `case_archive.csv` file or from built-in demo data.
- **Searching & Filtering:**  
  - Linear search for suspects and victims.  
  - Binary search for cases by ID (after sorting).
  - Filtering by crime type, severity, and status.
- **Sorting:** Uses merge sort to order cases by chosen attributes.

## Code Structure
- **Classes & Modules:**  
  - `Person`, `Suspect`, `Victim`: Representing individuals involved in a case.  
  - `Case`: Represents a single case with associated data.  
  - `CaseArchive`: Manages a collection of cases, providing methods to load, search, filter, and sort.  
  - `SortingAlgorithm` and `SearchAlgorithm`: Contain the logic for merge sort and searching methods.
  - `Application`: Runs the application and provides a text-base interface users can interactively choose operations to perform on the archive from. 
  
## Algorithms
- **Merge Sort:**  
  Used for sorting cases efficiently. Merge sort operates in O(n log n) time complexity, which is good for large datasets.
- **Binary Search:**  
  Utilized for searching cases by ID. Binary search operates in O(log n) time after sorting, making it efficient for searching large datasets.
- **Linear Search:**  
  Used for searching by suspect or victim name. Although O(n), this is sufficient for simpler searches.

## Exception Handling & Error Management
- Try-except blocks are used when loading CSV files and parsing data. If the CSV file is missing or improperly formatted, the application gracefully informs the user and provides options to load demo data.

## How to Run
1. Ensure you have Python 3 installed.
2. Place `case_archive.csv` in the same directory as the script (optional).
3. Run either `code.ipynb` or `code.py`.
4. Choose "Load Cases" to load data from the CSV, or load demo data if the CSV is not available.
5. Use the menu interface to explore search, filter, and sort functionalities.

## Requirements
- Python 3.x
- Standard Python libraries (`csv`, `datetime`).

## License
This project is for educational purposes as part of the Programming, Algorithms, and Data Structures course of the Copenhagen Business School MSc in Business Administration and Data Science. No specific license applies.