def simple_interest(p, t, r):
    print('The Principal is', p)
    print('The Time Period is', t)
    print('The Rate of Interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)


# Driver code
P = int(input("Please Enter the Principle Amount :"))
T = int(input("Please Enter the Time Period :"))
R = int(input("Please Enter the Rate of Interest :"))
simple_interest(P, T, R)
