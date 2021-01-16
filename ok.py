def main(harf):
  harflar = list(harf)
  soz = ''
  for h in harflar:
    if h == 'a':
      soz += 'а'
    elif h == 'b':
      soz += 'б'
    elif h == 'c':
      soz += 'с'
    elif h == 'd':
      soz += 'д'
    elif h == 'e':
      soz += 'е'
    elif h == 'f':
      soz += 'ф'
    elif h == 'g':
      soz += 'г'
    elif h == 'h':
      soz += 'х'
    elif h == 'i':
      soz += 'и'
    elif h == 'j':
      soz += 'ж'
    elif h == 'k':
      soz += 'к'
    elif h == 'l':
      soz += 'л'
    elif h == 'm':
      soz += 'м'
    elif h == 'n':
      soz += 'н'
    elif h == 'o':
      soz += 'о'
    elif h == 'p':
      soz += 'п'
    elif h == 'q':
      soz += 'q'
    elif h == 'r':
      soz += 'р'
    elif h == 's':
      soz += 'с'
    elif h == 't':
      soz += 'т'
    elif h == 'u':
      soz += 'у'
    elif h == 'v':
      soz += 'в'
    elif h == 'w':
      soz += 'w'
    elif h == 'x':
      soz += 'х'
    elif h == 'y':
      soz += 'й'
    elif h == 'z':
      soz += 'з'
    elif h == ' ':
      soz += ' '
  print(soz)

main('krill')