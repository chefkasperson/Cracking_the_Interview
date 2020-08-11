
def replace_spaces(string)
    new_string = ''
    string.chars.each do |c|
      if c == ' '
        c = '%20'
        new_string << c
      else
        new_string << c
      end
    end
    new_string
  end