import pyautogui
age = int(input("Enter your age: "))

if age < 18:
    pyautogui.alert("Age must be greater than or equal to 18")