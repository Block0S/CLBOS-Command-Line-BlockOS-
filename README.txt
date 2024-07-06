 --- CLBasic 1.1 Programming ---

NOTE: CLBOS Only runs in an IDE debugger, Such as Visual Studio Code for example.

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

Tie A Program
=========
NOTE: You cant enter the 'tap' Function in Line 9 Of the program you tied up.

If you type 'tap' In Line 9 Of the Code, you can type In Line 10 A Program you want to activate.
For This Example, The Program Is Named 'test1':

Line 1: print
Line 2: Hello
Line 3: 
Line 4: 
Line 5: 
Line 6: 
Line 7: 
Line 8: 
Line 9: tap
Line 10: test2

This Program will compile a program called 'test2' After a program called 'test1' is done compiling.

If Previous Vairable = [X] Then
==========

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