def palindrome_check(string)
    checked = {}
    odd_count = 0
    result = true
    string.chars.each do |c| 
      if checked[c]
        checked[c] += 1
      else
        checked[c] = 1
      end
    end
  
    checked.each do |key, value|
      if value % 2 != 0
        odd_count == 0 ? odd_count += 1 : result = false
      end
    end
    
    result
  
  end
  