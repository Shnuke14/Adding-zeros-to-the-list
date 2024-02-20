def do_stuff_with_number(n):
  print(n)

def catch_this():
  the_list = (1, 2, 3, 4, 5)

  for i in range(20):
    try:
      do_stuff_with_number(the_list[i])
    except IndexError:
      ## Вызывается при доступе к несуществуемому индексу списка
      do_stuff_with_number(0)

catch_this()