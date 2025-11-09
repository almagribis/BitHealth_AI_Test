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