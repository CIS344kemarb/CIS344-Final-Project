CREATE DATABASE hospital_portal;
CREATE TABLE patients (
    patient_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(45) NOT NULL,
    age INT NOT NULL,
    admission_date DATE,
    discharge_date DATE
);  

CREATE TABLE doctors (
    doctor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50),
    contact_number VARCHAR(15),
    email VARCHAR(100) UNIQUE
);
    
CREATE TABLE Appointments (
    appointment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctorS(doctor_id)
);
DELIMITER //

CREATE PROCEDURE ScheduleAppointment(
    IN patient_id INT,
    IN doctor_id INT,
    IN appointment_date DATE,
    IN appointment_time DECIMAL(5, 2)
)
BEGIN
    INSERT INTO Appointments (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (patient_id, doctor_id, appointment_date, appointment_time);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE DischargePatient(
    IN patient_id INT,
    IN discharge_date DATE
)
BEGIN
    UPDATE Patients
    SET discharge_date = discharge_date
    WHERE patient_id = patient_id;
END //

DELIMITER ;

INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES
    ('Sean Carter', 50, "2023-02-13", "2023-02-14"),  
    ('Ray Lewis', 32, "2023-11-11", "2023-11-20"),  
    ('Shawn Kemp', 52, "2023-05-26", "2023-06-02"); 
    
INSERT INTO doctors (doctor_name, specialization, contact_number, email) VALUES
    ('Dr. James', 'Dermatology', '+0342865449', 'dr.james@gmail.com'),
    ('Dr. Curry', 'Anesthesiology', '+9568760336', 'dr.curry@gmail.com');


