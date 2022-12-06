
print("Score evaluation program\n")

student_scoore = input("Insert student score please: ")

def evaluation(score):
    
    valoration="approve"
    if score<5:
        valoration="suspense"
    return valoration

print(evaluation(int(student_scoore)))

