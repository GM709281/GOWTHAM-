class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the function with different input lists of students
if __name__ == "__main":
  students = [
      Student("Alice", "A001", 3.5),
      Student("Bob", "B002", 3.2),
      Student("Charlie", "C003", 3.9),
      Student("David", "D004", 3.7),
      Student("Eve", "E005", 3.8),
  ]

  sorted_students = sort_students(students)

  print("Students sorted by CGPA (descending order):")
  for student in sorted_students:
      print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
