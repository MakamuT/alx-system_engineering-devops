#!/usr/bin/env ruby
#Script runs some statistics on the TextMe app
#puts ARGV[0].scan(/\[from:(.*?)\] /[to:(.*?)\] /[flags:(.*?)/).join(",")

if match = ARGV[0].match(/\[from:(.*?)\] /[to:(.*?)\] /[flags:(.*?)/).join(",")
                                                        sender = match[1]
                                                        receiver = match[2]
                                                        flags = match[3]
                                                        puts "#{sender},#{reciever},#{flags}"
else
  puts "No match found"
end
