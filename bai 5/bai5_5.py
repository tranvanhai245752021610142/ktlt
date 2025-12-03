def sort_list(lst):
    """Ham sap xep danh sach tang dan"""
    return sorted(lst)
def find_max(lst):
    """Ham tim phan tu lon nhat"""
    return max(lst)
def find_min(lst):
    """Ham tim phan tu nho nhat"""
    return min(lst)
n = int(input("Nhap so luong phan tu : "))
lst = []
for i in range(n):
    value = float(input(f"Nhap phan tu thu {i+1}: "))
    lst.append(value)
sorted_lst = sort_list (lst)
max_value = find_max(lst)
min_value = find_min(lst)
print("|nDanh sach ban dau:", lst)
print("Danh sach sau khi sap xep:", sorted_lst)
print("Phan tu lon nhat:", max_value)
print("phan tu nho nhat:", min_value)
