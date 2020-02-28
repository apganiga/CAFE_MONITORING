def search(a, search_item):
    low= 0
    high = len(a)-1
    Found = 0
    while low <= high:
        mid = (low + high) // 2
        print("low={}, high={}, mid={}, searching={}".format(low, high, mid, search_item))

        if a[mid] == search_item:
            Found = mid
            break
        elif a[mid] > search_item:
            high = mid -1
        elif a[mid] < search_item :
            low = mid + 1

    if Found == 0 :
        return -1
    else:
        return Found +1


a = [1,2,5,8,10,12,45,46,90,99]
# sorted list in increasing  order
# No duplicate in the list
search_item = int(input("Enter the element:"))
print(a)
print(search_item)
index_found = search(a, search_item)
print(index_found)





