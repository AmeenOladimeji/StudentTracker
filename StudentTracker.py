class Course:
    def __init__(self, course_code, course_title, course_credits, letter_grade, points):
        self.course_title = course_title
        self.course_code = course_code
        self.course_credits = course_credits
        self.letter_grade = letter_grade
        self.points = points
        
        #
class AcademicProgress():
    def __init__(self):
        self.student_dictionary = {'CMPT 101': Course('CMPT101', 'Intro to Computer Science',3,'A',12.0), 'MATH 114': Course('MATH 114', 'Elementary Calculus I', 3, 'B+', 9.9), 'CMPT 103': Course('CMPT103', 'Intro to Data Structures', 3, 'A-', 11.1), 'ENGL 102' : Course('ENGL 102', 'Analysis and Composition', 3, 'C', 6.0)}
        
    def banner(self): 
        print('================================================================================\n                    CAMPUS ACADEMIC PROGRESS ANALYZER v1.0\n================================================================================\n[SYSTEM] In-Memory Registry Active. No file configuration required.\n[SYSTEM] Pre-loading 4 Core Academic Course Objects...')
        print()        
     
    
    def main_menu(self):
        self.select_option = 0
        while self.select_option != 4:
 
 
            print('*** MAIN MENU ***\n1. View Complete Academic Transcript\n2. Calculate Live Cumulative GPA & Standings\n3. Add a New Completed Course Entry\n4. Exit Program\n')
            
        
            self.select_option = int(input('Select an option (1 - 4): ')) 
            if self.select_option == 1:
                self.option_one()
            
            elif self.select_option == 2:
                self.option_two()
                
            elif self.select_option == 3:
                self.option_three()
        
        if self.select_option == 4:
            self.option_four()
        print()
    def option_one(self):
        
        if self.select_option == 1:
            self.total_credits = 0
            for course in self.student_dictionary.values():
                self.total_credits += course.course_credits
                
            print('================================================================================\n                          OFFICIAL ACADEMIC TRANSCRIPT\n================================================================================\nCourse Code     | Course Title                  | Credits | Letter Grade | Points')
                
            for k , v in self.student_dictionary.items():
                target_width = 30
                spaces_off = target_width - len(v.course_title)
                padding = ' ' * spaces_off 
                
                print(f"{k}\t| {v.course_title}{padding}| {v.course_credits} \t  | {v.letter_grade}\t\t | {v.points}  ")
               
            print('================================================================================')
            print(f'TOTAL ATTEMPTED CREDITS: {self.total_credits}')
            print()
            self.main_menu() 
            
            
    def option_two(self):
        self.total_credits = 0
        quality_points = 0
        gpa = 0
        for k ,v in self.student_dictionary.items():
            self.total_credits += float(v.course_credits)
            quality_points += float(v.points)
            gpa = (quality_points) / (self.total_credits)
        print('================================================================================\n                            ACADEMIC PERFORMANCE METRIC\n================================================================================')
        print(f'Total Completed Courses: {len(self.student_dictionary.keys())}')
        print(f'Total Earned Credits : {self.total_credits}')
        print(f'Total Quality Points: {quality_points}\n')
        print(f'>>> CURRENT CUMULATIVE GPA: {gpa} / 4.00')
        
        if gpa >= 3.50:
            print('>>> ACADEMIC STANDING     : Good Standing (Dean\'s List Eligible')
        elif gpa >= 2.00 and gpa < 3.50:
            print('>>> ACADEMIC STANDING     : Good Standing')
        else:
            print('>>> ACADEMIC STANDING     : Academic Probation')
        print()
        
    def option_three(self):
        print('--- ADD NEW COURSE ENTRY ---')
        new_course_code = input('Enter Course Code (e.g., STAT 151): ')
        new_course_title = input('Enter Course Title: ')
        new_course_credits = int(input('Enter Credits (1-4): '))
        new_points = int(input('Enter points received: '))
        new_letter_grade = input('Enter Letter Grade Received (A+, A, B, etc.):')
        print()
        self.student_dictionary[new_course_code] = Course(new_course_code, new_course_title, new_course_credits, new_letter_grade, new_points)
        print(f'[SUCCESS] {new_course_code} has been added to your academic record!')
        
    def option_four(self):
        print('[SYSTEM] Flushing in-memory records... Shutting down program.\nGoodbye!')
        exit()
        
        
grades = AcademicProgress()
grades.banner()
grades.main_menu()
