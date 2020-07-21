def check_permutation(string1, string2)
    str1 = string1.chars.sort
    str2 = string2.chars.sort
    str1 == str2 ? true : false
end