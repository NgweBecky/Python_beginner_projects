def sockMerchant(n, ar):
    result = 0
    socks = {}
    # lets loop our array and find our pairs
    for elt in ar:
        # if the color is already in our dictionary
        #increment the element value by 1
        #else add the element to the dic with value 1
        if elt not in socks.keys():
            socks[elt] = 1

        else:
            socks[elt] += 1
    
    for key in socks.keys():
        result += socks[key]//2
    return result

n = input("enter the total number of socks: ").strip()
#map does a typecasting of each string element in the list
#to an integer
ar = list(map(int, input("enter the socks present: ").strip().split()))
total = sockMerchant(n, ar)
print(f"the total pair(s) of sock(s): {total}")
