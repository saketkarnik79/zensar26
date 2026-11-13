
import sqlite3
import pandas as pd

# Step 1: Connect to SQLite database
connection = sqlite3.connect("company.db")

try:
    # Step 2: Create employee table
    connection.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            EmployeeID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Department TEXT,
            Salary REAL
        )
    """)

    # Reset sample data for repeatable execution
    connection.execute("DELETE FROM Employees")

    # Step 3: Insert records
    employees = [
        (101, "Amit", "IT", 50000),
        (102, "Priya", "HR", 45000),
        (103, "Rahul", "Finance", 60000),
        (104, "Neha", "IT", 55000)
    ]

    connection.executemany("""
        INSERT INTO Employees
        (EmployeeID, Name, Department, Salary)
        VALUES (?, ?, ?, ?)
    """, employees)

    connection.commit()

    # Step 4: Read records
    print("Original Employee Records:")

    df = pd.read_sql_query(
        "SELECT * FROM Employees",
        connection
    )

    print(df)

    # Step 5: Update a record
    connection.execute("""
        UPDATE Employees
        SET Salary = ?
        WHERE EmployeeID = ?
    """, (65000, 103))

    connection.commit()

    # Step 6: Delete a record
    connection.execute("""
        DELETE FROM Employees
        WHERE EmployeeID = ?
    """, (102,))

    connection.commit()

    # Step 7: Read filtered records
    high_salary = pd.read_sql_query("""
        SELECT *
        FROM Employees
        WHERE Salary > ?
        ORDER BY Salary DESC
    """, connection, params=(50000,))

    print("\nEmployees Earning Above 50000:")
    print(high_salary)

    # Step 8: Department-wise aggregation
    summary = pd.read_sql_query("""
        SELECT
            Department,
            COUNT(*) AS EmployeeCount,
            SUM(Salary) AS TotalSalary,
            AVG(Salary) AS AverageSalary
        FROM Employees
        GROUP BY Department
    """, connection)

    print("\nDepartment Summary:")
    print(summary)

except sqlite3.Error as error:
    connection.rollback()
    print("Database Error:", error)

finally:
    connection.close()
