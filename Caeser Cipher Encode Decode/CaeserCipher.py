
# Tool to decrypt/encrypt with Caesar cipher (or Caesar code), a shift cipher, one of the most easy and most famous encryption systems, that uses the substitution of a letter by another one further in the alphabet.

# Example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar,

# so check it out and try it once

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount,cipher_direction):
  end_text=""
  for letter in start_text:
    if letter in alphabet:
      position=alphabet.index(letter)
      if cipher_direction=="encode":
        new_position=position+shift_amount
        end_text+=alphabet[new_position]
      else:
        new_position=position-shift_amount+26
        end_text+=alphabet[new_position]
    else:
      end_text+=letter

  print(f"The {cipher_direction}d text is {end_text}")

from art import logo
print(logo)

should_continue=True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  
  caesar(text,shift,direction)

  last=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  if last=="no":
    print("Goodbye\n")
    should_continue=False
    
 
