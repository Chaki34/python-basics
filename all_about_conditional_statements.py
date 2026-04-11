# =====================================================
#  PYTHON CONDITIONAL STATEMENTS PRACTICE
# author: Debmalya chaki
# Date : 2026-04-12
# =====================================================

# Step 1: Display heading
print("===== CONDITIONAL STATEMENTS DEMO =====")


# =====================================================
#  1. SIMPLE IF STATEMENT
# =====================================================

# Step 2: Assign a value
age = 18

# Step 3: Check condition using if
if age >= 18:
    print("You are eligible to vote")


# =====================================================
#  2. IF - ELSE STATEMENT
# =====================================================

# Step 4: Take a number
num = 7

# Step 5: Check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# =====================================================
#  3. IF - ELIF - ELSE STATEMENT
# =====================================================

# Step 6: Assign marks
marks = 85

# Step 7: Grade system
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# =====================================================
#  4. NESTED IF STATEMENT
# =====================================================

# Step 8: Assign values
age = 20
has_id = True

# Step 9: Nested condition check
if age >= 18:
    if has_id:
        print("Allowed to enter")
    else:
        print("ID required")
else:
    print("Not allowed")


# =====================================================
#  5. MULTIPLE CONDITIONS (LOGICAL OPERATORS)
# =====================================================

# Step 10: Assign values
username = "admin"
password = "1234"

# Step 11: Check login condition
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# =====================================================
#  6. SWITCH CASE (MATCH-CASE IN PYTHON)
# =====================================================

# Step 12: Take operator input
operator = '+'

# Step 13: Use match-case (Python 3.10+)
match operator:
    case '+':
        print("You selected Addition")
    case '-':
        print("You selected Subtraction")
    case '*':
        print("You selected Multiplication")
    case '/':
        print("You selected Division")
    case _:
        print("Invalid operator")


# =====================================================
# CONDITIONAL EXAMPLES
# =====================================================

print("\n=====  CONDITIONAL EXAMPLES =====")

# Step 14: Prediction threshold (classification)
probability = 0.7

if probability > 0.5:
    print("AI Prediction: Positive")
else:
    print("AI Prediction: Negative")


# Step 15: Accuracy check
accuracy = 0.82

if accuracy >= 0.9:
    print("Excellent Model")
elif accuracy >= 0.7:
    print("Good Model")
else:
    print("Needs Improvement")


# Step 16: Feature check
features = ["age", "income", "score"]

if "income" in features:
    print("Feature 'income' is used in model")


# Step 17: Loss comparison
loss = 0.3

if loss < 0.2:
    print("Low Loss")
else:
    print("High Loss")


# Step 18: Access control (AI system rule)
is_logged_in = True
has_permission = False

if is_logged_in and has_permission:
    print("Access Granted")
else:
    print("Access Denied")


# =====================================================
#  END OF PROGRAM
# =====================================================