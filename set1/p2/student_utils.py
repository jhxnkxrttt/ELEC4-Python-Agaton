
# Agaton, Jhon Kurt V. IV-BSIT B
# P2: Custom Module - student_utils


# Function 1: Compute average
def compute_average(grades):
    return sum(grades) / len(grades)


# Function 2: Determine pass or fail
def grade_status(grades):
    average = compute_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 3: Get highest grade
def get_high_grade(grades):
    return max(grades)


# Function 4: Get lowest grade
def get_low_grade(grades):
    return min(grades)
