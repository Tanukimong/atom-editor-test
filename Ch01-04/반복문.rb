i = 0
while i<10 do
  puts('puts("Hello world '+(i*9).to_s()+'")')
  i = i+1
  if i==4
    break #Break the while문
  end
end
