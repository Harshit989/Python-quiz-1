import random

# Sample quiz questions for each subject (with options)
quiz_questions = {
    "Operating System": [
        ("What is a process?", ["A. A program in execution", "B. An inactive program", "C. A CPU", "D. A file"], "A"),
        ("What is a thread?", ["A. A single process", "B. A lightweight process", "C. A hardware component", "D. A network protocol"], "B"),
        ("What is virtual memory?", ["A. Physical memory", "B. Hardware memory", "C. A memory management technique", "D. Cache memory"], "C"),
        ("What is a system call?", ["A. A program request to the OS", "B. A type of interrupt", "C. A hardware failure", "D. None of the above"], "A"),
        ("What is a kernel?", ["A. The shell of the OS", "B. The core of the OS", "C. A hardware abstraction", "D. A program", "B"]),
        ("What is a deadlock?", ["A. A memory management problem", "B. An OS crash", "C. A situation where processes are stuck", "D. A synchronization mechanism"], "C"),
        ("What is an interrupt?", ["A. A signal to the CPU", "B. A type of cache", "C. A type of semaphore", "D. A memory address"], "A"),
        ("What is paging?", ["A. A CPU scheduling method", "B. A memory management technique", "C. A file management technique", "D. A threading model"], "B"),
        ("What is a semaphore?", ["A. A data structure", "B. A communication tool", "C. A synchronization tool", "D. A memory management technique"], "C"),
        ("What is context switching?", ["A. A thread switching mechanism", "B. A deadlock prevention mechanism", "C. A process switching mechanism", "D. None of the above"], "A"),
    ],
    "Database Management System": [
        ("What is a DBMS?", ["A. A data management software", "B. A hardware device", "C. A network protocol", "D. An operating system"], "A"),
        ("What is SQL?", ["A. Structured Query Language", "B. Sequential Query Language", "C. Standard Query Language", "D. Secure Query Language"], "A"),
        ("What is a primary key?", ["A. A unique identifier", "B. A foreign key", "C. A key for encryption", "D. A database record"], "A"),
        ("What is normalization?", ["A. The process of creating databases", "B. Organizing data to reduce redundancy", "C. Writing complex queries", "D. Ensuring security"], "B"),
        ("What is a foreign key?", ["A. A key from another table", "B. A unique key", "C. A primary key", "D. A composite key"], "A"),
        ("What is indexing?", ["A. A way to sort and search data", "B. A method for organizing queries", "C. A form of data replication", "D. A type of backup"], "A"),
        ("What is a transaction?", ["A. A database operation", "B. A single unit of work", "C. A query", "D. A table"], "B"),
        ("What is ACID?", ["A. Properties of a database", "B. A type of query", "C. A form of encryption", "D. A user authentication method"], "A"),
        ("What is a query?", ["A. A request for data", "B. A database", "C. A primary key", "D. A transaction"], "A"),
        ("What is a relational model?", ["A. A model of data storage", "B. A way to relate data", "C. A set of data in tables", "D. An encryption model"], "C"),
    ],
    "Computer Network": [
        ("What is a protocol?", ["A. A set of rules for communication", "B. A hardware device", "C. A software application", "D. A transmission method"], "A"),
        ("What is TCP/IP?", ["A. A type of protocol", "B. A network architecture", "C. A communication standard", "D. A data encryption method"], "B"),
        ("What is the OSI model?", ["A. A set of security protocols", "B. A layered network model", "C. A software tool", "D. A hardware component"], "B"),
        ("What is a router?", ["A. A device for routing data", "B. A data link layer device", "C. A network protocol", "D. A network cable"], "A"),
        ("What is DNS?", ["A. Domain Name System", "B. Data Network System", "C. Dynamic Name System", "D. Domain Network Service"], "A"),
        ("What is DHCP?", ["A. Data Handling Control Protocol", "B. Dynamic Host Configuration Protocol", "C. Domain Host Configuration Protocol", "D. Data Host Connection Protocol"], "B"),
        ("What is a MAC address?", ["A. A hardware address", "B. A software key", "C. An IP address", "D. A network cable"], "A"),
        ("What is an IP address?", ["A. A unique identifier for a device", "B. A hardware component", "C. A network protocol", "D. An encryption standard"], "A"),
        ("What is a switch?", ["A. A device to forward data", "B. A layer 3 device", "C. A software tool", "D. A network protocol"], "A"),
        ("What is a subnet?", ["A. A division of an IP network", "B. A type of encryption", "C. A protocol", "D. A hardware device"], "A"),
    ]
}

# To store user registration details
users_db = {}

# Function to register a student
def register_student():
    print("\n--- Registration ---")
    name = input("Enter your name: ")
    reg_id = input("Create a registration ID: ")
    password = input("Create a password: ")

    if reg_id in users_db:
        print("Registration ID already exists. Please try again.")
        return register_student()

    users_db[reg_id] = {"name": name, "password": password, "attempted_quizzes": {}}
    print(f"Registration successful. Your registration ID is {reg_id}.")

# Function to log in a student
def login_student():
    print("\n--- Login ---")
    reg_id = input("Enter your registration ID: ")
    password = input("Enter your password: ")

    if reg_id in users_db and users_db[reg_id]["password"] == password:
        print(f"Login successful. Welcome, {users_db[reg_id]['name']}!")
        return reg_id
    else:
        print("Invalid registration ID or password. Please try again.")
        return login_student()

# Function to take quiz
def take_quiz(subject, reg_id):
    questions = quiz_questions[subject]
    already_attempted = users_db[reg_id]["attempted_quizzes"].get(subject, [])

    # Get 5 random questions
    while True:
        selected_questions = random.sample(questions, 5)
        if selected_questions != already_attempted:
            break

    print(f"\n--- {subject} Quiz ---")
    score = 0

    for i, (question, options, answer) in enumerate(selected_questions, 1):
        print(f"Q{i}: {question}")
        for option in options:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == answer:
            score += 1

    # Store the attempted questions for reattempt prevention
    users_db[reg_id]["attempted_quizzes"][subject] = selected_questions

    print(f"\nYou scored {score}/5 in the {subject} quiz.")
    return score

# Function to choose subject
def choose_subject():
    print("\n--- Choose Subject ---")
    print("1. Operating System")
    print("2. Database Management System")
    print("3. Computer Network")
    subject_choice = input("Enter your choice (1/2/3): ")

    if subject_choice == "1":
        return "Operating System"
    elif subject_choice == "2":
        return "Database Management System"
    elif subject_choice == "3":
        return "Computer Network"
    else:
        print("Invalid choice. Please try again.")
        return choose_subject()

# Main function to handle registration, login, and quiz
def main():
    while True:
        print("\n--- Welcome to the Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            register_student()
        elif choice == "2":
            reg_id = login_student()
            while True:
                subject = choose_subject()
                take_quiz(subject, reg_id)
                reattempt = input("Do you want to reattempt the quiz? (yes/no): ").strip().lower()
                if reattempt != "yes":
                    break
        elif choice == "3":
            print("Thank you for using the Quiz Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
