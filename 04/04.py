# def range_subset(range1, range2):
#     """Whether range1 is a subset of range2."""
#     if not range1:
#         return True  # empty range is subset of anything
#     if not range2:
#         return False  # non-empty range can't be subset of empty range
#     if len(range1) > 1 and range1.step % range2.step:
#         return False  # must have a single value or integer multiple step
#     return range1.start in range2 and range1[-1] in range2


file_obj = open("input.txt", "r")
counter = 0
counter2 = 0
for line in file_obj:
    line = line.strip('\n')
    line = line.split(',')
    nums1 = line[0].split('-')
    nums2 = line[1].split('-')
    num1_1 = int(nums1[0])
    num1_2 = int(nums1[1])
    
    num2_1 = int(nums2[0])
    num2_2 = int(nums2[1])
    
    if num1_1 >= num2_1 and num1_2 <= num2_2:
        counter +=1
        counter2 +=1
    elif num2_1 >= num1_1 and num2_2 <= num1_2:
        counter +=1
        counter2 +=1
    elif num1_1 <= num2_1 and num1_2 >= num2_1:
        counter2 +=1
    elif num2_1 <= num1_1 and num2_2 >= num1_1:
        counter2 +=1
        
    
print(counter2)
print(counter)