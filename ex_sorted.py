#numbers = ["20240903_11","20240903_12","20240903_13"]
import os
folderName = os.listdir("test")
print(folderName)
sorted_numbers_desc = sorted(numbers, reverse=False)
print(f"정렬:{sorted_numbers_desc}")