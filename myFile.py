#Dean Woelfle
#12/16/2020
#Lab 4
#Project Euler Problems 1 - 13

#Lets the user select a problem
Problem = input("Type a number to choose a problem. Possible problems: 1 - 13 \n")
print("")

#problem 1
if (Problem == '1'):

    #reads prompt of problem
    print("Find the sum of all the multiples of 3 or 5 below 1000.\n")
    #total
    sum = 0
    #runs through every number from 1 to 1000
    for num in range(1, 1000):

        #sees if it is divisible by 3
        if (num % 3 == 0):
            #if so, adds it to total
            sum += num 
        #sees if it is divisible by 3
        elif (num % 5 == 0):
            #if so, adds it to total
            sum += num 
    #turns total into a string
    sum = str(sum)
    #prints out answer (total)
    print("The sum of all the multiples of 3 or 5 below 1000 is " + sum)

#problem 2
elif (Problem == '2'):

    #reads prompt of problem
    print("Each new term in the Fibonacci sequence is generated by adding the previous two terms.\nBy considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.\n")
    #List for Fibonacci sequence
    FibList = [1,2]
    #total
    sum = 0
    #makes sure sequence doesn't go above four million
    while ((FibList[-1]+FibList[-2]) < 4000000):
        #adds most recent to second most recent value in sequence to get newest value
        FibList.append(FibList[-1]+FibList[-2])

    #runs through all values in sequence and sees if they are divisible by 2 (even)
    for num in FibList:
        if (num % 2 == 0):
            #if so, adds it to total
            sum += num
    #turns total into a string
    sum = str(sum)
    #prints out answer (total)
    print("The sum of all the even valued terms less than four million in the Fibonacci sequence is " + sum)

#problem 3
elif (Problem == '3'):

    #reads prompt of problem
    print("What is the largest prime factor of the number 600851475143?")

    #list for calculated prime factors
    primes = []

    #goes through a list of numbers (the reason I chose 10,000 as a max was to reduce computation time. Our final answer is less than 10,000 so this works. This number can be increased, but raises the computation time)
    for num in range(1, 10000):
        #sees if the number is even a factor
        if (600851475143 % num == 0):
            prime = True
            #sees if the number is prime
            for numm in range(1,num):
                if (num % numm == 0 and numm != 1 and numm != num):
                    prime = False
            #if it is prime, adds it to the list of primes
            if (prime == True):
                primes.append(num)
                print(num)
    #selects and prints the most recent (so the largest) prime
    primee = str(primes[-1])
    print("\nThe largest prime factor of the number 600851475143 is " + primee)

#problem 4
elif (Problem == '4'):

    #reads prompt of problem
    print("Find the largest palindrome made from the product of two 3-digit numbers\n")

    #getting some variables ready 
    num1 = 100
    num2 = 100
    palindromic = 0
    
    #runs through all the 3 digit numbers for variable 1
    while (num1 != 1000):
        #runs through all the 3 digit numbers for variable 2
        while (num2 != 1000):
            #multiplies them together
            value = num1 * num2
            #checks if the product is palindromic
            if str(value) == (str(value))[::-1]:
                #checks if the palindrome is the highest so far
                if palindromic < value:
                    #if so, saves the values to print later
                    palindromic = value
                    m1 = str(num1)
                    m2 = str(num2)
            #cycles to next number
            num2 += 1
        num2 = 100
        num1 += 1

    #prints out result
    val = str(value)
    print("The largest palindrome made from the product of two 3-digit numbers is " + val + "\n" + m1 + " * "  + m2)

#problem 5
elif (Problem == '5'):

    #reads prompt of problem
    print ("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n(takes a bit to load)\n")

    #num starts at 1, goes up one at a time
    num = 1

    #loops until break
    while 1==1:
        #goes through denominators 1 through 20, making sure they all are divisible evenly
        if num % 2 == 0:
            if num % 3 == 0:
                if num % 4 == 0:
                    if num % 5 == 0:
                        if num % 6 == 0:
                            if num % 7 == 0:
                                if num % 8 == 0:
                                    if num % 9 == 0:
                                        if num % 10 == 0:
                                            if num % 11 == 0:
                                                if num % 12 == 0:
                                                    if num % 13 == 0:
                                                        if num % 14 == 0:
                                                            if num % 15 == 0:
                                                                if num % 16 == 0:
                                                                    if num % 17 == 0:
                                                                        if num % 18 == 0:
                                                                            if num % 19 == 0:
                                                                                if num % 20 == 0:
                                                                                    #prints out result
                                                                                    nu = str(num)
                                                                                    print("the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is " + nu)
                                                                                    #breaks loop
                                                                                    break
        #cycles to next number                                                                        
        num += 1

#problem 6
elif (Problem == '6'):  

    #reads prompt of problem
    print("Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n")

    #resets variables
    num = 1
    current = 0

    #running through and adding up all the squares
    while (num != 101):
        current += num ** 2
        num += 1
    #saving this value
    top = current

    #resets variables
    num = 1
    current = 0

    #running through and adding up all the numbers
    while (num != 101):
        current += num
        num += 1
    #squares result
    bottom = current ** 2

    #calculates the answer
    diff = bottom - top

    #converts numbers to strings for print statement
    diff = str(diff)
    top = str(top)
    bottom = str(bottom)
    
    #prints out result
    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is " + diff + "\n" + bottom + " - " + top + " = " + diff)

#problem 7
elif (Problem == '7'):  

    #reads prompt of problem
    print("What is the 10,001st prime number?\n(takes a bit to load)\n")

    '''getting our variables ready. 
    The reason I already start at a prime counted is because I'm skipping 2 and starting at 3.
    This allows the line 'for i in range(2, num):' to function correctly as num has to be at least 1 number larger than 2.'''
    primecount = 1
    num = 3

    #produces primes until the 10,001st prime is made
    while (primecount != 10001):
        #runs through all denominators EXCEPT 1 and itself (for efficient prime calculations, saving computing time)
        for i in range(2, num):
            #assumes number is prime, tries to prove otherwise
            prime = True
            #if the number is divisible by any other (besides 1 and intself), the number is proven to not be prime and the for loop is broken to save time
            if num % i == 0:
                prime = False
                break
        #checks if the number is prime
        if (prime == True):
            #adds to the prime count and saves the number as most recent prime
            primecount += 1
            pri = str(num)
        #goes onto the next number
        num += 1

    #prints out result
    print("The 10,001st prime number is " + pri)
        
#problem 8
elif (Problem == '8'):  

    #reads prompt of problem
    print("Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?\n")

    #the 1000 digit number
    number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    #setting up counting variables
    temp = 0
    final = 0

    #setting up 1-13 positional variables
    f1 = 0
    f2 = 1
    f3 = 2
    f4 = 3
    f5 = 4
    f6 = 5
    f7 = 6
    f8 = 7
    f9 = 8
    f10 = 9
    f11 = 10
    f12 = 11
    f13= 12
    
    #runs until count is over the 1000th digit place
    while (f13 != 1000):
        #multiplied 13 adjacent digits
        temp = int(number[f1]) * int(number[f2]) * int(number[f3]) * int(number[f4]) * int(number[f5]) * int(number[f6]) * int(number[f7]) * int(number[f8]) * int(number[f9]) * int(number[f10]) * int(number[f11]) * int(number[f12]) * int(number[f13])
        
        #moves all the 1-13 positional variables up 1 place
        f1 += 1
        f2 += 1
        f3 += 1
        f4 += 1
        f5 += 1
        f6 += 1
        f7 += 1
        f8 += 1
        f9 += 1
        f10 += 1
        f11 += 1
        f12 += 1
        f13 += 1

        #sees if this is the greatest number found so far
        if (temp > final):
            #if so, saves it
            final = temp

            #saves the specific place values for these numbers, as they product the greatest product
            ff1 = str(f1)
            ff2 = str(f2)
            ff3 = str(f3)
            ff4 = str(f4)
            ff5 = str(f5)
            ff6 = str(f6)
            ff7 = str(f7)
            ff8 = str(f8)
            ff9 = str(f9)
            ff10 = str(f10)
            ff11 = str(f11)
            ff12 = str(f12)
            ff13 = str(f13)
            ffinal = str(final)

    #prints out our solution
    print("The thirteen adjacent digits in the 1000-digit number that have the greatest product have positions " + ff1 + ", " + ff2 + ", " + ff3 + ", " + ff4 + ", " + ff5 + ", " + ff6 + ", " + ff7 + ", " + ff8 + ", " + ff9 + ", " + ff10 + ", " + ff11 + ", " + ff12 + ", and " + ff13 + "\nThe value of this product is " + ffinal)

#problem 9
elif (Problem == '9'):  

    #reads prompt of problem
    print("There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.")

    #variables for a, b, and c to be increased
    numa = 1
    numb = 1
    numc = 1
    #To be used to see if the answer has been found, as to not waste time
    found = False
    
    #runs until answer is found
    while found == False:

        #running through c, if it gets too big b goes up and c gets set to b
        numc += 1
        if numc > 500:
            numc = numb
            numb += 1

        #running through b, if it gets too big a goes up and b gets set to a
        if numb > 500:
            numb = numa
            numa += 1

        #if the variables form a Pythagorean triplet
        if (numa ** 2 + numb ** 2 == numc ** 2):
            #if they add to 1000
            if (numa + numb + numc == 1000):
                found = True
                #getting variables ready to be printed
                prod = numa * numb * numc
                prod = str(prod)
                numa = str(numa)
                numb = str(numb)
                numc = str(numc)

    #prints out our solution
    print("the three numbers are " + numa + ", " + numb + ", and " + numc + "\nThe product abc is " + prod)

#problem 10
elif (Problem == '10'):

    #reads prompt of problem
    print("Find the sum of all the primes below two million. (takes a bit to load)")

    #gets counting variables ready. This code is heavily reused from #7
    summ = 2
    numm = 3
    #while our number being tested for primeness is under 2 million
    while (numm < 2000000):
        #tests if the number is prime 
        for i in range(2, numm):
            #assumes it is prime, tries to prove otherwise
            prime = True
            if numm % i == 0:
                #if it is composite, breaks to save time
                prime = False
                break
        #if the number is prime, adds it to the total so far
        if (prime == True):
            summ += numm
        #moves onto the next candidate for a prime
        numm += 1
    
    #gets variable ready to print
    summ = str(summ)

    #prints out our solution
    print("The sum of all the primes below two million is " + summ)

#problem 11
elif (Problem == '11'):

    #reads prompt of problem
    print("What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?\n")

    #list of all 400 numbers
    listt = [8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8, 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00, 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65, 52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91, 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80, 24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50, 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70, 67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21, 24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95, 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92, 16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57, 86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58, 19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40, 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66, 88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36, 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16, 20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54, 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
    
    '''At first this problem really confused me, but I realised that if I think of horizontal, verticle, and diagonal patterns
    in the grid as position changes then it would be a lot easier. For example, straight horizontal lines move 1 every time, 
    horizontal move 20 (moving to a new line), diagonal down to the left is 19 (moving down a line but minus 1), and
    diagonal down to the right is 21 (moving down a line plus 1).
    '''

    #counting variables
    prodh = 0
    spot = 0

    #horizontal line (1 count)
    while(spot < 397):
        #adding up four points
        prod = listt[spot] * listt[spot+1] * listt[spot+2] * listt[spot+3]
        #if highest so far
        if prod > prodh:
            #saving variables
            prodh = prod
            sa = spot + 1
            sb = spot + 2
            sc = spot + 3
            sd = spot + 4
        #moving up 1
        spot += 1
    #resseting count
    spot = 0

    #diagonal down to the left (19 count)
    while(spot < 343):
        #adding up four points
        prod = listt[spot] * listt[spot+19] * listt[spot+38] * listt[spot+57]
        #if highest so far
        if prod > prodh:
            #saving variables
            prodh = prod
            sa = spot + 1
            sb = spot + 20
            sc = spot + 39
            sd = spot + 58
            #moving up 1
        spot += 1
    #resseting count
    spot = 0

    #verticle line (20 count)
    while(spot < 340):
        #adding up four points
        prod = listt[spot] * listt[spot+20] * listt[spot+40] * listt[spot+60]
        #if highest so far
        if prod > prodh:
            #saving variables
            prodh = prod
            sa = spot + 1
            sb = spot + 21
            sc = spot + 41
            sd = spot + 61
            #moving up 1
        spot += 1
    #resseting count
    spot = 0

    #diagonal down to the right (21 count)
    while(spot < 337):
        #adding up four points
        prod = listt[spot] * listt[spot+21] * listt[spot+42] * listt[spot+63]
        #if highest so far
        if prod > prodh:
            #saving variables
            prodh = prod
            sa = spot + 1
            sb = spot + 22
            sc = spot + 43
            sd = spot + 64
            #moving up 1
        spot += 1

    #converting final variables to strings
    sa = str(sa)
    sb = str(sb)
    sc = str(sc)
    sd = str(sd)
    prodh = str(prodh)

    #prints out our solution
    print("The greatest product of four adjacent numbers in the same direction in the 20×20 grid is " + prodh + "\nThe 4 numbers were in positions " + sa + ", " + sb + ", " + sc + ", and " + sd + " out of 400.")

#problem 12
elif (Problem == '12'):

    #reads prompt of problem
    print("What is the value of the first triangle number to have over five hundred divisors? (takes a long time to load)")

    #setting up number variables for counting/calculations
    num = 1
    add = 1
    count = 1
    amount = 0

    #loops until found
    found = False
    while found == False:
        
        #running through possible denominators
        while count <= num:
            #sees if remainder is equal to 0 to see if it is divisible
            if num % count == 0:
                #adds a count
                amount += 1
            
            #goes on to next denominator
            count += 1
            
            #checks if there are over 500
            if amount > 500:
                #cuts the loop and changes answer to string as we're done
                found = True
                numf = str(num)
        
        #changes amounts for next loop
        amount = 0
        count = 1
        add += 1
        num += add

    #prints solution
    print("The value of the first triangle number to have over five hundred divisors is " + numf)
    
#problem 13
elif (Problem == '13'):
     
    #the 5000 numbers
    numbers = [37107287533902102798797998220837590246510135740250,
    46376937677490009712648124896970078050417018260538,
    74324986199524741059474233309513058123726617309629,
    91942213363574161572522430563301811072406154908250,
    23067588207539346171171980310421047513778063246676,
    89261670696623633820136378418383684178734361726757,
    28112879812849979408065481931592621691275889832738,
    44274228917432520321923589422876796487670272189318,
    47451445736001306439091167216856844588711603153276,
    70386486105843025439939619828917593665686757934951,
    62176457141856560629502157223196586755079324193331,
    64906352462741904929101432445813822663347944758178,
    92575867718337217661963751590579239728245598838407,
    58203565325359399008402633568948830189458628227828,
    80181199384826282014278194139940567587151170094390,
    35398664372827112653829987240784473053190104293586,
    86515506006295864861532075273371959191420517255829,
    71693888707715466499115593487603532921714970056938,
    54370070576826684624621495650076471787294438377604,
    53282654108756828443191190634694037855217779295145,
    36123272525000296071075082563815656710885258350721,
    45876576172410976447339110607218265236877223636045,
    17423706905851860660448207621209813287860733969412,
    81142660418086830619328460811191061556940512689692,
    51934325451728388641918047049293215058642563049483,
    62467221648435076201727918039944693004732956340691,
    15732444386908125794514089057706229429197107928209,
    55037687525678773091862540744969844508330393682126,
    18336384825330154686196124348767681297534375946515,
    80386287592878490201521685554828717201219257766954,
    78182833757993103614740356856449095527097864797581,
    16726320100436897842553539920931837441497806860984,
    48403098129077791799088218795327364475675590848030,
    87086987551392711854517078544161852424320693150332,
    59959406895756536782107074926966537676326235447210,
    69793950679652694742597709739166693763042633987085,
    41052684708299085211399427365734116182760315001271,
    65378607361501080857009149939512557028198746004375,
    35829035317434717326932123578154982629742552737307,
    94953759765105305946966067683156574377167401875275,
    88902802571733229619176668713819931811048770190271,
    25267680276078003013678680992525463401061632866526,
    36270218540497705585629946580636237993140746255962,
    24074486908231174977792365466257246923322810917141,
    91430288197103288597806669760892938638285025333403,
    34413065578016127815921815005561868836468420090470,
    23053081172816430487623791969842487255036638784583,
    11487696932154902810424020138335124462181441773470,
    63783299490636259666498587618221225225512486764533,
    67720186971698544312419572409913959008952310058822,
    95548255300263520781532296796249481641953868218774,
    76085327132285723110424803456124867697064507995236,
    37774242535411291684276865538926205024910326572967,
    23701913275725675285653248258265463092207058596522,
    29798860272258331913126375147341994889534765745501,
    18495701454879288984856827726077713721403798879715,
    38298203783031473527721580348144513491373226651381,
    34829543829199918180278916522431027392251122869539,
    40957953066405232632538044100059654939159879593635,
    29746152185502371307642255121183693803580388584903,
    41698116222072977186158236678424689157993532961922,
    62467957194401269043877107275048102390895523597457,
    23189706772547915061505504953922979530901129967519,
    86188088225875314529584099251203829009407770775672,
    11306739708304724483816533873502340845647058077308,
    82959174767140363198008187129011875491310547126581,
    97623331044818386269515456334926366572897563400500,
    42846280183517070527831839425882145521227251250327,
    55121603546981200581762165212827652751691296897789,
    32238195734329339946437501907836945765883352399886,
    75506164965184775180738168837861091527357929701337,
    62177842752192623401942399639168044983993173312731,
    32924185707147349566916674687634660915035914677504,
    99518671430235219628894890102423325116913619626622,
    73267460800591547471830798392868535206946944540724,
    76841822524674417161514036427982273348055556214818,
    97142617910342598647204516893989422179826088076852,
    87783646182799346313767754307809363333018982642090,
    10848802521674670883215120185883543223812876952786,
    71329612474782464538636993009049310363619763878039,
    62184073572399794223406235393808339651327408011116,
    66627891981488087797941876876144230030984490851411,
    60661826293682836764744779239180335110989069790714,
    85786944089552990653640447425576083659976645795096,
    66024396409905389607120198219976047599490197230297,
    64913982680032973156037120041377903785566085089252,
    16730939319872750275468906903707539413042652315011,
    94809377245048795150954100921645863754710598436791,
    78639167021187492431995700641917969777599028300699,
    15368713711936614952811305876380278410754449733078,
    40789923115535562561142322423255033685442488917353,
    44889911501440648020369068063960672322193204149535,
    41503128880339536053299340368006977710650566631954,
    81234880673210146739058568557934581403627822703280,
    82616570773948327592232845941706525094512325230608,
    22918802058777319719839450180888072429661980811197,
    77158542502016545090413245809786882778948721859617,
    72107838435069186155435662884062257473692284509516,
    20849603980134001723930671666823555245252804609722,
    53503534226472524250874054075591789781264330331690]

    #base to add to
    total = 0

    #adds each number
    for num in numbers:
        total += num

    #converts to string
    anslong = str(total)

    #prints first 10 characters if string, being our solution
    print("The first ten digits of the one-hundred 50-digit numbers are " + anslong[0:10])


#problem failed to enter
else:
    print("Error: You didn't input a problem correctly")
