


puts 'How are you deaf grandma? and input what you what to say grandma'
words = gets.chomp 

while words != 'BYE'
    if words == words.upcase 
        year = 1930 + rand(20)
        puts 'NO, NOT SINCE ' + year.to_s + '!'
    else 
        puts 'HUH?! SPEAK UP , SONNY!'
    end 
    words = gets.chomp 
end
