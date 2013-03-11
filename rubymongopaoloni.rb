require 'rubygems'

require 'mongo'

include Mongo

 

db   = Connection.new.db('sample-db')

coll = db.collection('test')

 

coll.remove

3.times do |i|

  coll.insert({'a' => i+1})

end

puts "There are #{coll.count()} records. Here they are:"

coll.find().each { |doc| puts doc.inspect }
