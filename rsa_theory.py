import sys, getopt, base64

# globals
prime1 = 67
prime2 = 79
k = 3
e = 5

# encode operations
def encode(data):
    # encoding data using RSA theory
    encrypted = ''
    commas = 0
    encryptedstring = ''
    n = calculate_n()
    for element in data:
        encrypted = pow(ord(element), e, n)
        #print(encrypted)
        encryptedstring = encryptedstring + str(encrypted)
        if commas < (len(data) - 1):
            encryptedstring = encryptedstring + ","
            commas += 1
    return encryptedstring

# decode operations
def decode(data):
    # decode data using RSA theory
    d = calculate_d()
    n = calculate_n()
    decryptedphrase = ''
    for datum in data:
        decryptedcode = pow(int(datum), d, n)
        decryptedchar = chr(decryptedcode)
        decryptedphrase = decryptedphrase + decryptedchar
    decryptedphrase = decodeb64(decryptedphrase)
    return decryptedphrase

# base64 encode string
def encodeb64(datastring):
    data_bytes = datastring.encode('ascii')
    base64_bytes = base64.b64encode(data_bytes)
    base64_datastring = base64_bytes.decode('ascii')
    return base64_datastring

# base64 decode string
def decodeb64(datastring):
    base64_bytes = datastring.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return(message)

# Calculate the phi of N
def calculatephiofn():
    phiofn = (prime1 - 1) * (prime2 - 1)
    return phiofn

# Calculate N derived from the prime numbers
def calculate_n():
    enn = prime1 * prime2
    return enn

# Calculate the private key
def calculate_d():
    pofn = calculatephiofn()
    dee = (k * pofn + 1) / e
    return int(dee)

# Main function
def main(argv):
    dstring = ''
    encrypt = 'n'
    decrypt = 'n'
    
    try:
        opts, args = getopt.getopt(argv, "heds:", ["help", "encrypt", "decrypt", "string="])
    except getopt.GetoptError:
        print ('rsa_theory.py -heds <string>')
        sys.exit(2)
    for opt, arg in opts:

        if opt in ("-h", "--help"):
            print(
            '''
            rsa_theory.py <options>
            -h --help: This help output
            -e --encrypt: encrypt data
            -d --decrypt: decrypt data
            -s --string: string of data to encrypt or decrypt
            '''
            )
            sys.exit()
        elif opt in ("-e", "--encrypt"):
            encrypt = 'y'
        elif opt in ("-d", "--decrypt"):
            decrypt = 'y'
        elif opt in ("-s", "--string"):
            dstring = arg
            
    # Call functions and print results
    if encrypt == 'y':
        dstring = encodeb64(dstring)
        print(dstring)
        encoded = encode(dstring)
        print(encoded)

    if decrypt == 'y':
        decodestring = dstring.split(",")
        decodestring = decode(decodestring)
        print(decodestring)

# Let's get everything running.
if __name__ == '__main__':
    main(sys.argv[1:])
