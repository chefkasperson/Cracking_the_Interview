def roman_numerals(n):
      list = []
  string = ""
  while n > 0:
    if n > 1000:
      n -= 1000
      list.append("M")
    elif n > 900:
      n -= 900
      list.append("CM")
    elif n > 500:
      n -= 500
      list.append("D")
    elif n > 400:
      n -= 400
      list.append("CD")
    elif n > 100:
      n -= 100
      list.append("C")
    elif n > 90:
      n -= 90
      list.append("XC")
    elif n > 50:
      n -= 50
      list.append("L")
    elif n > 40:
      n -= 40
      list.append("XL")
    elif n > 10:
      n -= 10
      list.append("X")
    elif n == 9:
      n -= 9
      list.append('IX')
    elif n >= 5:
      n -= 5
      list.append("V")
    elif n == 4:
      n -= 4
      list.append("IV")
    else:
      n -= 1
      list.append("I")
  
  return string.join(list)


# def solution(n):
#     roman_numerals = {
#         1000:'M',
#         900: 'CM',
#         500: 'D',
#         400: 'CD',
#         100: 'C',
#         90: 'XC',
#         50: 'L',
#         40: 'XL',
#         10: 'X',
#         9: 'IX',
#         5: 'V',
#         4: 'IV',
#         1: 'I'
#     }
#     roman_string = ''
#     for key in sorted(roman_numerals.keys(),reverse=True):
#         while n >= key:
#             roman_string += roman_numerals[key]
#             n -= key
#     return roman_string