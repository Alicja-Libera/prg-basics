####
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f'Title in capital letters:', {movie.upper()})

# print title in small letters
print(f'Title in small letters:', {movie.lower()})

# print how many times the vowel "e" appears in the title
print(f'How many times the "e" appears:', {movie.count("e")})


# print where in the text is the word "Lord"
print(f'where in the text is the word "Lord": ', {movie.find('Lord')})


# print where in the text is the word "dragon"
print(f'where in the text is the word "dragon": ', {movie.find('dragon')})
