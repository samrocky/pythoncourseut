a1 = input()
a2 = input()
a3 = input()
b1 = input()
b2 = input()
b3 = input()
c1 = input()
c2 = input()
c3 = input()
print("{:^15}|{:^15}|{:^15}|{:^15}".format("first name", "last name", "age", "email"))
print("{:^15}|{:^15}|{:^15}|{:^15}".format(a1, a2, a3, "{}.{}.{}@gmail.com".format(a1.lower(), a2.lower(), a3.lower())))
print("{:^15}|{:^15}|{:^15}|{:^15}".format(b1, b2, b3, "{}.{}.{}@gmail.com".format(b1.lower(), b2.lower(), b3.lower())))
print("{:^15}|{:^15}|{:^15}|{:^15}".format(c1, c2, c3, "{}.{}.{}@gmail.com".format(c1.lower(), c2.lower(), c3.lower())))