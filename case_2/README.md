# SQL for Patient Visit Insight

This project demonstrates how to run a **patient visit insight query** using:

- Sample CSV datasets (`patients`, `visits`, `symptoms`)
- A Jupyter Notebook (`setup_db.ipynb`) to load csv file and save to db
- A SQLite database (`hospital_records.db`) that contain tables  (`patients`, `visits`, `symptoms`)
- A Jupyter Notebook (`perform_query.ipynb`) to load the DB and execute a query from `query.sql`

The notebook provides a full workflow example:
1. Load and store CSV data into a single SQLite database.
2. Execute an analytical SQL query from an external file.
3. Display the query results.

---

## Goals

Execute a query that:

- Finds the **5 most recent visits** to the **Neurology** department  
- Where the patient had **at least 3 recorded symptoms**  
- And the patient is **older than 50 years**

Expected output columns:

- `patients.name`
- `patients.age`
- `visits.visit_date`
- `symptom_count`

## Installation

Make sure Python is installed, then install dependencies:

```bash
pip install pandas
```

## How to Run
### Setup DB
1. Prepare the following CSV files:
- patients.csv
- visits.csv
- symptoms.csv
2. Open the notebook `setup_db.ipynb`.
3. Adjust csv filepath and db name.
4. Run all cells in order.
5. The notebook will save the db `data`.

### Perform Query
1. Open the notebook `setup_db.ipynb`.
2. Run all cells in order.
3. Notebook will open `query.sql` file and execute.

## Query
```
SELECT
    patients.name,
    patients.age,
    visits.visit_date,
    COUNT(symptoms.id) as symptom_count
FROM patients
JOIN visits ON patients.id = visits.patient_id
JOIN symptoms ON visits.id = symptoms.visit_id
WHERE visits.department = "Neurology" AND patients.age > 50
GROUP BY patients.name, patients.age, visits.visit_date
HAVING COUNT(symptoms.id) >= 3
ORDER BY visits.visit_date DESC
LIMIT 5;
```

## Output
| name  | age | visit_date           | symptom_count |
|--------|-----|----------------------|----------------|
| Dimas  | 53  | 2025-10-10 00:00:00 | 4              |
| Zara   | 72  | 2025-06-05 00:00:00 | 3              |
| Omar   | 70  | 2025-03-20 00:00:00 | 3              |
| Citra  | 62  | 2025-01-12 00:00:00 | 3              |
