# Nama    : Jesiva Trivena Sinaga
# NIM     : A11.2021.13808
# Kelomok : A11.4329

def prepare_text(plain_text):
    # Ganti J dengan I
    plain_text = plain_text.replace('J', 'I')
    # Hilangkan spasi dan ubah menjadi huruf kapital
    plain_text = ''.join(plain_text.split()).upper()
    # Tambahkan 'X' jika panjang teks ganjil
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    return plain_text

def prepare_key(key):
    # Ganti J dengan I
    key = key.replace('J', 'I')
    key = ''.join(key.split()).upper()
    # Buat bujur sangkar 5x5
    key_square = [['' for _ in range(5)] for _ in range(5)]
    used_letters = set()
    i, j = 0, 0
    for letter in key:
        if letter not in used_letters:
            key_square[i][j] = letter
            used_letters.add(letter)
            j += 1
            if j == 5:
                j = 0
                i += 1
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for letter in alphabet:
        if letter not in used_letters:
            key_square[i][j] = letter
            used_letters.add(letter)
            j += 1
            if j == 5:
                j = 0
                i += 1
    return key_square
def find_position(key_square, letter):
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == letter:
                return i, j
def playfair_encrypt(plain_text, key):
    plain_text = prepare_text(plain_text)
    key_square = prepare_key(key)
    ciphertext = ''
    for i in range(0, len(plain_text), 2):
        letter1 = plain_text[i]
        letter2 = plain_text[i + 1]
        row1, col1 = find_position(key_square, letter1)
        row2, col2 = find_position(key_square, letter2)
        if row1 == row2:
            ciphertext += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_square[row1][col2] + key_square[row2][col1]
    return ciphertext

# Input teks dan kunci
plain_text = input("Masukkan plaintext: ")
key = input("Masukkan kunci: ")

# Enkripsi teks
cipher_text = playfair_encrypt(plain_text, key)

print("Ciphertext: " + cipher_text)
