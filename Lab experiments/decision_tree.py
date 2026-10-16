
def predict(hours, attendance):
    if hours >= 6:
        if attendance >= 75:
            return "Pass"
        else:
            return "Fail"
    else:
        if attendance >= 85:
            return "Pass"
        else:
            return "Fail"

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

result = predict(hours, attendance)

print("Predicted Result:", result)
