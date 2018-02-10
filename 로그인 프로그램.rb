puts("아이디를 입력하시오")
input_id = gets.chomp()
members = ['egoing','k8805','leezche']
for member in members do
  if member == input_id
    puts('Hello!, '+member)
    exit
  end
end

puts('Who are you?')
