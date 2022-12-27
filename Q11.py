import pyautogui
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a < b:
    if a == 4 and b == 9:
        for i in range(a,b+1):
            print(i)
else:
    pyautogui.alert("Please give first number small and second number large")