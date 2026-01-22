#เราใช้ in ไม่ได้เพราะเราต้องการคำ นั้นเดี่ยวๆ
#เราจึงต้องสแกนทีละตัวนั้นเอง

# Input interested word
key = input().strip()

# Input text
text = input().strip()

# Remove symbol from the text
new_text = ""
for char in text:
    if char in ['"', "(", ")", ",", ".", "'"]:
        new_text += " "
    else:
        new_text += char

# Split the new text into words
words = new_text.split()

# Count the occurrences of the interested word
count = 0
for word in words:
    if word == key:
        count += 1

# Output the count
print(count)