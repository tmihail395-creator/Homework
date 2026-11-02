# > < <= >= == !=(не дорівнює)
# and or not
time=int(input("Enter number at seconds? "))
choise=int(input("Введіть свій вибір: 1- години 2- хвилини"))
hour =0
minets=0
if choise == 1:
    hour=time//3600
    print(f"Hours left {hour}")
elif choise == 2:
    minets=time//60
    print(f"Minets left {minets}")