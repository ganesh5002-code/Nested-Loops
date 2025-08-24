# Decimal to binary conversion

# Ask user what decimal number they want to convert
decimal = int(input("Enter a decimal number:"))

# Find highest power of 2 less than decimal
exponent = 1
while exponent<=decimal:
    exponent *= 2
exponent //=2

binary = ''

while exponent > 0:
    for i in range(1):
        if decimal>=exponent:
            binary+= '1'
            decimal-=exponent
        else:
            binary+='0'
    exponent //=2
print("The binary number is", binary)    