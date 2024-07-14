# A Note From Wish

Smaller version of CLBOS (SmallCL.py)
is
Meant to be offered as a *Special Version*
This code may take longer to update.
Please list the cons in the Version.
Tool used: https://freecodingtools.org/online-minifier/python
Pros:
- 223 Bytes Saved
Cons:
- Less Updates
- Might take longer
- Beta build (May not work on many systems!)
--- CLBasic 1.2 Programming ---

NOTE: CLBOS Only runs in an IDE debugger, Such as Visual Studio Code for example.

To code, Type "clbasic" after debugging and entering your password.

Printing
=========
To print, type "print" (in lowercase) in the line you want.
And In the line after that write what you want to print.

Inputs
=========
To input, type "inp" (in lowercase) in the line you want.
And In the line after that write what you want to be in the input.
For Example:

Line 1: inp
Line 2: username

That Would be compiled to "username $ " With the input box after that.
Note that after an input is entered, it will print it.

Math Inputs
=========
Math inputs are basically inputs, but with math.
if you type 'minpp', it will compile into 2 inputs: First / Second.
Then, after the 2 inputs her set, It will add them up.
There are more minp combinations: minpm (minus), minpmu (multiply), minpd (divide).

Smart Inputs
=========
Smart Inputs (sminp) are basically Math Inputs, But with only 1 input. The Second input is set in the next line of the code.
For Example:

Line 1: sminpp
Line 2: 200

If the first input the user gives is "100", then it will print 300.
Other Combinations of Smart Inputs: sminpm (minus), sminpmu (multiply), minpd (divide)

Saving Variables
=========
NOTE: You cant save variables & read variables in the same script, cause is still unknown.

If you type 'svb', it will compile and save a variable with the name of it being the next line of the code, and the data inside of it being the next-next line of the code.
For Example:

Line 1: svb
Line 2: myVariable
Line 3: Hello World

This will compile into saving a variable named 'myVariable' with the text 'Hello World' Inside of it.

Reading Variables
=========
NOTE: You cant save variables & read variables in the same script, cause is unknown yet.

If you type 'rvb', it will compile into reading a variable with the name of it being the next line of the code.
For Example:

Line 1: rvb
Line 2: myVariable

This will compile into reading a variable named 'myVariable'.

If Previous Vairable = [X] Then
==========
NOTE: This doesnt work anymore, You can still put this in your code (And not get an error) But It will just not function.

If you type 'ipi' (Starting In Line 3 of the script until line 7), you can type in the next line what value you want the previous input to be to print a string of text,
And In the line after the string of text is what will be printed if The Previous Variable DOESNT Equal to that value.
For Example:

Line 1: inp
Line 2: 1 + 1
Line 3: ipi
Line 4: 2
Line 5: Correct
Line 6: Incorrect

That Will Compile into an input box. that if the user gives the value '2' to it it will say 'Correct', and If otherwise; it will say 'Incorrect'.
