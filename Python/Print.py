# SIMPLE COMMAND
print("HELLO WORLD")  #SIMPLE COMMANT FOR OUTPUT TEXT
#------------------------------------------------------------------------------------------------------------
name = "vasya PUPKIN" # VAR name =
print (name.title())  # Vasya Pupkin  in output because add title()
print(name.upper())   # name = "VASYA PUPKIN" in output because add upper()
print (name.lower())  # name = vasya pupkin  in output because add lower()
#------------------------------------------------------------------------------------------------------------
a = " // Hello//."    # New var a
print(a.rstrip())     # Delete " " from right part(r- right)
print(a.lstrip())     # Delete " " from left part (l- left)
print(a.strip(" ""/"".")) # Delete " " and "/" "." from a  (Hello) without / .
b = (a.strip(" ""/""."))  # New b
print(b)                  # Print new vars b
# ------------------------------------------------------------------------------------------------------------
#FOR
# EXAMPLE1
for x in range(0, 100):           # Create Number 0-99 ,(100 not be in this)
    print("NUMBER=" + str(x))

# FOR +BREAK
# EXAMPLE2
for c in range(0, 100):
    print("num=" + str(c))
    if c == 50:                  # IF C=50 command loops end
        break
#TO BE 100 in OUTPUT
# EXAMPLE3
for v in range (0, 100 + 1):     # Create Number 0-100(100 be in this) because add 100+1
    print(v)
# WITH STEPS 5
# EXAMPLE4
for b in range (0, 100 + 1, 5):  # Create with steps "5" 10-15-20-25.....
    print(b)





