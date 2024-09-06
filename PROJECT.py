import sqlite3

def get_connection():
    return sqlite3.connect('school_management.db')

def add_student(name, dob, grade):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Students (name, dob, grade) VALUES (?, ?, ?)', (name, dob, grade))
        conn.commit()
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
    finally:
        conn.close()

def view_students():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Students')
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
        rows = []
    finally:
        conn.close()
    return rows

def update_student(student_id, name, dob, grade):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE Students SET name = ?, dob = ?, grade = ? WHERE student_id = ?', (name, dob, grade, student_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
    finally:
        conn.close()

def delete_student(student_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Students WHERE student_id = ?', (student_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
    finally:
        conn.close()

def main():
    while True:
        print('\nSchool Management System')
        print('1. Add Student')
        print('2. View Students')
        print('3. Update Student')
        print('4. Delete Student')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            name = input('Enter student name: ')
            dob = input('Enter student date of birth (YYYY-MM-DD): ')
            grade = input('Enter student grade: ')
            add_student(name, dob, grade)
            print('Student added successfully.')
        
        elif choice == '2':
            students = view_students()
            if students:
                for student in students:
                    print(student)
            else:
                print('No students found.')
        
        elif choice == '3':
            student_id = int(input('Enter student ID to update: '))
            name = input('Enter new student name: ')
            dob = input('Enter new student date of birth (YYYY-MM-DD): ')
            grade = input('Enter new student grade: ')
            update_student(student_id, name, dob, grade)
            print('Student updated successfully.')
        
        elif choice == '4':
            student_id = int(input('Enter student ID to delete: '))
            delete_student(student_id)
            print('Student deleted successfully.')
        
        elif choice == '5':
            print('Exiting...')
            break
        
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
