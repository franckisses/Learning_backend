# 99 bottels of wall 

bottles_of_beer = 99

puts bottles_of_beer 

while bottles_of_beer != 1
    puts bottles_of_beer.to_s + ' bottles of beer on the wall,'+ bottles_of_beer.to_s + ' bottles of beer'
    bottles_of_beer = bottles_of_beer - 1 
    puts 'Take on down and pass it around,' + bottles_of_beer.to_s + ' bottles of beer on the wall'
    if bottles_of_beer == 1
        puts bottles_of_beer.to_s + ' bottles of beer on the wall' + bottles_of_beer.to_s + '  bottles of beer'
        puts 'Take on down and pass it around, no more bottles of beer on the wall'
    end 
end 

puts 'No more bottles of beer on the wall, no more bottles of beer'
puts 'Go to the store and buy some more, 99 bottles of beer on the wall'