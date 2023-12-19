import mysql.connector
from mysql.connector import Error

class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="hospital_portal",
                 user='root',
                 password='Sasuke14!'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def addPatient(self, patient_name, age, admission_date, discharge_date):
        ''' Method to insert a new patient into the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (patient_name, age, admission_date, discharge_date))
            self.connection.commit()
            return

    def getAllPatients(self):
        ''' Method to get all patients from the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM patients"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllAppointments(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM appointments"  
            self.cursor.execute(query)
            appointments = self.cursor.fetchall()
            return appointments

    def scheduleAppointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        ''' Method to schedule an appointment '''
        if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
                data = (patient_id, doctor_id, appointment_date, appointment_time)
                self.cursor.execute(query, data)
                self.connection.commit()
                
        pass

    def viewAppointments(self):
        ''' Method to view all appointments '''
        if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "SELECT * FROM appointments"
                self.cursor.execute(query)
                appointments = self.cursor.fetchall()
                return appointments
            
        pass

    def dischargePatient(self, patient_id):
        ''' Method to discharge a patient '''
        if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "Discharge patient WHERE patient_id = %s"
                data = (patient_id,)
                self.cursor.execute(query, data)
                self.connection.commit()
                
        pass

    def viewAllDoctors(self):
        ''' Method to view all doctors '''
        if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "SELECT * FROM doctors"
                self.cursor.execute(query)
                doctors = self.cursor.fetchall()
                return doctors

        pass

    def viewRecords(self):
        ''' Method to view all doctors '''
        if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = '''
                    SELECT
                        A.appointment_id,
                        A.appointment_date,
                        A.appointment_time,
                        D.doctor_id,
                        D.doctor_name,
                        D.specialization,
                        D.contact_number AS doctor_contact,
                        D.email AS doctor_email,
                        P.patient_id,
                        P.patient_name,
                        P.age,
                        P.admission_date,
                        P.discharge_date
                    FROM
                        appointments A
                        JOIN doctors D ON A.doctor_id = D.doctor_id
                        JOIN patients P ON A.patient_id = P.patient_id;
                '''
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                return records

        pass

    def updatePatientDetails(self, patient_id, new_name, new_age):
        ''' Method to update patient details '''
        if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "UPDATE patients SET patient_name = %s, age = %s WHERE patient_id = %s"
                data = (new_name, new_age, patient_id)
                self.cursor.execute(query, data)
                self.connection.commit()

        pass


