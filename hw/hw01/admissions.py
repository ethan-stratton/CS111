import csv

# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
	
# define your functions here

def grade_improvement(grades):
    """
    Returns True if the average score of each semester is higher than or equal to each previous semester and False otherwise.
    Hint: investigate how the == operator works between two lists and think about using the Python's sorted() function.
    """
    for i in range(1, len(grades)):
        if grades[i] < grades[i - 1]:
            return False
    return True


def grade_outlier(grades):
    """
    takes in a list of grades (of any length) and returns True if one single number is more than 20 points lower than all other numbers; otherwise, False.
    Example:
    Input: [99, 94, 87, 89, 56, 78, 89]
    Hint: Sort the list from lowest to highest, and check for the difference between the two lowest grades.
    78 - 56 = 22; 22 > 20
    Output: True
    """
    #follow Hint
    sorted_grades = sorted(grades)
    
    if sorted_grades[1] - sorted_grades[0] > 20:
        return True
    else:
        return False

def calculate_score_improved(grades):
    """
    calculates a student score, checks if it is an outlier, and returns True 
    if the student has a score of 6 or higher OR was flagged as an outlier; 
    otherwise, return False. 
    """
    #calculate score
    total_score = calculate_score(grades)
    #check if outlier
    outlier_status = is_outlier(grades)

    if total_score >= 6 or outlier_status:
        return True
    else:
        return False


def is_outlier(grades):
    """
    if the demonstrated interest score is 0 
    
    or if the normalized GPA that is more than 2 points higher than the normalized SAT score.
    If either of these conditions is true, it should return True (because this student is an outlier); 
    otherwise, the function returns False.
    """
    #Ma Mayhem ,1380,4.3,8,1
    #for some reason she passes through, though she shouldn't

    sat_score, gpa, interest, _ = grades
    
    if interest == 0:
        return True
    else:
        normalized_gpa = gpa * 2  
        normalized_sat = sat_score / 160

        if normalized_gpa > normalized_sat + 2: 
            return True
        else:
            return False

def calculate_score(grades):
    """
    Input: [1300.0,3.61,10.0,7.0] - which represents a student with a 1300 SAT score, a 3.61 GPA, 10 out of 10 for interest and 7 out of 10 for high school quality
    Output: ((1300 / 160) * 0.3) + ((3.61 * 2) * 0.4) + (10 * 0.1) + (7 * 0.2) = 7.73 out of 10
    """
    #30% SAT, 40% GPA, 10% demonstrated interest, 20% strength of curriculum
    sat_score, gpa, interest, high_school_quality = grades
    sat_contribution = (sat_score / 160) * 0.3
    gpa_contribution = (gpa * 2) * 0.4
    interest_contribution = interest * 0.1
    high_school_quality_contribution = high_school_quality * 0.2
    total_score = (
        sat_contribution
        + gpa_contribution
        + interest_contribution
        + high_school_quality_contribution
    )
    return total_score


def convert_row_type(nums):
    return [float(i) for i in nums]


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")    
    
    data = []

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()

    #loop through the lists contents
    #Make use of the str.split(delimiter) function to break individual lines into a list of elements. 
    #Make sure that you've done this by printing your list after using the split() function. 
    #You'll delete this print statement later but make sure to double check this before moving on! 
    for line in input_file:
        data_line = line.split(',')
        data.append(data_line)
        #Once you have each line in a list, save the student's name in a variable, then delete the name from your list.
        #save name, perform float function, conjoin together again
        prospective_student_name = data_line[0]
        data_line.remove(prospective_student_name)
        #send numbers to function
        data_line = convert_row_type(data_line)
        if not check_row_types(data_line):
            print("Please check the row to ensure it is of list size 8.")

        #Separate your data. Use list slicing to separate your list (which should contain 8 numbers at this point) 
        #into two lists: one that contains the student's SAT, GPA, Interest, and High School Quality scores, 
        #and one that contains their 4 semester grades. 
            
        #should I modify the existing list or make two new ones?
        student_aggregate_data = data_line[0:4]
        student_semester_grades = data_line[4:8]

        student_score = "{:.2f}".format(calculate_score(student_aggregate_data)) #saves only to two decimal places
        check_outlier_status = is_outlier(student_aggregate_data)
        
        #write to student_scores.csv such that each row contains a student’s name and their score, separated by a comma.
        with open('student_scores.csv', 'a', newline='') as file: #done as "a" for "append" and not "w" for "write" so we don't rewrite
            #writer = csv.writer(file)
            #writer.writerow([prospective_student_name, student_score])
            # the above code caused a big error because of carriage handlind differences, don't forget to have consistency
            file.write(prospective_student_name+ ',' + student_score + '\n')

        #if the student has a score of 6 or higher, put them in a new csv called chosen_students.csv
        if float(student_score) >= 6:
            with open('chosen_students.csv', 'a', newline='') as chosen_students_file:
                chosen_students_file.write(prospective_student_name + '\n')
        
        #looking for outliers
        if check_outlier_status:
            with open('outliers.csv', 'a', newline='') as outlying_students_file:
                outlying_students_file.write(prospective_student_name + '\n')

        #Ma Mayhem ,1380,4.3,8
        
        #Write students' names, one per line, to the file chosen_improved.csv 
        #if they either have a score of 6 or greater OR if they are an outlier 
        #and their score is 5 or greater. 
        if float(student_score) >= 6 or (check_outlier_status and float(student_score) >= 5):
            with open('chosen_improved.csv', 'a', newline='') as chosen_improved_file:
                chosen_improved_file.write(prospective_student_name + '\n')

        #Call calculate_score_improved() from your main() and output each student’s information 
        #(name, SAT, GPA, interest score, and high school quality) to a new file called 
        #better_improved.csv if calculate_score_improved() returned True for them.
        if calculate_score_improved(student_aggregate_data):
            with open('better_improved.csv', 'a', newline='') as better_improved_file:
                student_string = ','.join([str(i) for i in student_aggregate_data])
                better_improved_file.write(f"{prospective_student_name},{student_string}\n")

        #part 5
        #if grade_outlier(student_semester_grades):
        #    print(f"Student {prospective_student_name} has a single grade outlier.")
                
        # consider the importance of an algorithm being able to flag students who might have a lower overall 
        # GPA but have shown improvement over time.
                
        # chose all students if they either have a score of 6 or greater or if they have a score of 5 or more and at least one of the following is true:
        #is_outlier() returns True, grade_outlier() returns True, or grade_improvement() returns True
        if float(student_score) >= 6 or (
            float(student_score) >= 5 and (
                is_outlier(student_aggregate_data) or grade_outlier(student_semester_grades) or grade_improvement(student_semester_grades)
                )
            ):
            with open('composite_chosen.csv', 'a', newline='') as composite_file:
                composite_file.write(prospective_student_name + '\n')

    #print(headers)
    #print(data)

    #make sure to close all files
    input_file.close()

    #result = is_outlier((1380, 4.3, 8, 1))
    #print(result) #should be False, returns True

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
