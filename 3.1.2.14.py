blocks = int(input("Enter the number of blocks: "))
height=0
layer_size=1
if blocks <= 0: height = 0
else:
    while blocks:
        blocks -= layer_size
        if blocks < 0: break
        height += 1
        layer_size += 1
#
# Write your code here.
#

print("The height of the pyramid:", height)