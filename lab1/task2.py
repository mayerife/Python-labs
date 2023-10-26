BYTES_PER_SYMBOL = 4

diskette_mb = 1.44
pages = 100
lines = 50
symbols = 25
mb_in_bytes = 1024 * 1024

diskette_byte = diskette_mb * mb_in_bytes
book_byte = pages * lines * symbols * BYTES_PER_SYMBOL
num_books = diskette_byte // book_byte

print("Количество книг, помещающихся на дискету:", int(num_books))
