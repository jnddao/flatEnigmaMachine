# gets inputs from user
def getInputs():
    # starting position
    print("Please enter 3 letter starting position in ALL CAPS: ", end = '')
    sPosition = input()
    
    # rotor order
    print("Please enter rotorOrder (eg 123 with default reflector b): ", end = '')
    rotorOrder = input()

    # request coded msg
    print("Please enter coded message IN ALL CAPS: ", end = '')
    code = input().replace(" ", "")

    return sPosition, rotorOrder, code

# get's the next letter of a rotor given the next array being array
# used for both alphabet and random cipher
def getForward(rPointer, rLetter, array):
    if (rPointer > 25) : 
        rPointer = rPointer - 26

    iNum = rPointer

    for letter in array[rPointer:]:
        if letter == rLetter:
            break
        else:
            iNum += 1
    
    return iNum

# gets the reflector given the 'reflectee' 
# reference is the given letter
# ref is the array of letters
# curr is the position currently pointing at
def getRef(reference, ref, curr):
    i = 0
    for char in ref:
        if char == reference and i != curr:
            return i
        else : 
            i += 1


# yucky main function
# added one more repetition to rotors to help prevent end of array errors
# only ment for short words and NOT sentences
# removes spaces but does not support full stops
def main() :
    # required rotors and references
    rotor1String = "EKMFLGDQVZNTOWYHXUSPAIBRCJEKMFLGDQVZNTOWYHXUSPAIBRCJEKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2String = "AJDKSIRUXBLHWTMCQGZNPYFVOEAJDKSIRUXBLHWTMCQGZNPYFVOEAJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3String = "BDFHJLCPRTXVZNYEIWGAKMUSQOBDFHJLCPRTXVZNYEIWGAKMUSQOBDFHJLCPRTXVZNYEIWGAKMUSQO"
    refString = "ABCDEFGDIJKGMKMIEBFTCVVJAT"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # splitting to avoid long array declarations
    alp = list(alphabet)
    ref = list(refString)
    rotor1 = list(rotor1String)
    rotor2 = list(rotor2String)
    rotor3 = list(rotor3String)
    temp = [[], [], []]

    # added +1 toggles
    toggle1 = [17, 43] 
    toggle2 = [5, 31] 
    toggle3 = [22, 48]
    tempToggle = [[], [], []]

    # gets the first positions of the rotors 
    # and all other needed user input data
    sPosition, rotorOrder, code = getInputs()

    # sets the starting positions by the static alphabet 
    # assuming doesnt change by rotor
    r1 = ord(sPosition[0]) - 65
    r2 = ord(sPosition[1]) - 65
    r3 = ord(sPosition[2]) - 65

    # loop to set rotor order
    counter = 0
    for num in list(str(rotorOrder)):
        if num == "1":
            temp[counter] = rotor1.copy()
            tempToggle[counter] = toggle1.copy()
        elif num == "2":
            temp[counter] = rotor2.copy()
            tempToggle[counter] = toggle2.copy()
        elif num == "3":
            temp[counter] = rotor3.copy()
            tempToggle[counter] = toggle3.copy()

        counter += 1
    
    # setting rotor order
    rotor1 = temp[0]
    rotor2 = temp[1]
    rotor3 = temp[2]
    toggle1 = tempToggle[0]
    toggle2 = tempToggle[1]
    toggle3 = tempToggle[2]

    # enigma loop!
    for char in code:
        r3 += 1 # increment 3rd by 1

        # check if they all have to be incremented
        if r3 in toggle3:r2 += 1
        if r2 in toggle2:r1 += 1
        if r1 in toggle1:
            pass # wth happens here????
        
        # check if any of the rs are over 51. Will set to 0 otherwise.
        # still need to do edge cases where rotor is at the end or key is greater than array reaches
        if (r3 > 51): r3 = 0
        if (r2 > 51): r2 = 0
        if (r1 > 51): r1 = 0


        # number to keep track of position
        # getFoward is position of alp
        # first half of encryption
        curr = (ord(char) - 65) + r3 # get the initial position

        curr = getForward(r3, rotor3[curr], alp)
        curr = r2 + curr - r3
        curr = getForward(r2, rotor2[curr], alp)
        curr = r1 + curr - r2
        curr = getForward(r1, rotor1[curr], alp)

        # getting reflection and starting again
        reference = ref[curr - r1]
        curr = getRef(reference, ref, curr - r1)
   
        # second half of encryption
        # gerForward is location of rotor
        curr = curr + r1
        curr = getForward(r1, alp[curr], rotor1)
        curr = r2 + curr - r1
        curr = getForward(r2, alp[curr], rotor2)
        curr = r3 + curr - r2
        curr = getForward(r3, alp[curr], rotor3)

        # printing
        print("%s" % alp[curr - r3], end = '')
    # end of line
    print ("")


if __name__ == "__main__":
    main()
