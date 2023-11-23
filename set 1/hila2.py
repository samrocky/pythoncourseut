a_1 = input()

a_2 = input()

a_3 = input()

b_1 = input()

b_2 = input()

b_3 = input()

c_1 = input()

c_2 = input()

c_3 = input()



print("{:^15}|{:^15}|{:^15}|{:^15}".format("first name", "last name", "age", "email"))
print("{:^15}|{:^15}|{:^15}|{:^15}".format(a_1, a_2, a_3, "{}.{}.{}@gmail.com".format(a_1.lower(), a_2.lower(), a_3.lower())))
print("{:^15}|{:^15}|{:^15}|{:^15}".format(b_1, b_2, b_3, "{}.{}.{}@gmail.com".format(b_1.lower(), b_2.lower(), b_3.lower())))
print("{:^15}|{:^15}|{:^15}|{:^15}".format(c_1, c_2, c_3, "{}.{}.{}@gmail.com".format(c_1.lower(), c_2.lower(), c_3.lower())))