non_alpha = "!?',;."
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
for i in non_alpha:
    paragraph.replace(i, "")
print(paragraph)
    
