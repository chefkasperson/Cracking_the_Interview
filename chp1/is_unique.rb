def is_unique(string)
    found = {}
    string.chars.each do |letter|
        if found[letter]
            return false
        else
            found[letter] = true
        end
    end
    true
end