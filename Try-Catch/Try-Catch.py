# Lets Lear about try catch block.
try:
  f = open("xyz.txt", "a")
  f.write("Hello Guys!")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
