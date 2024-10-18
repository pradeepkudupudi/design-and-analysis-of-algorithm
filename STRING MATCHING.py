text = "Hello, this is a simple text string."
pattern = "simple"

text_length = len(text)
pattern_length = len(pattern)

for i in range(text_length - pattern_length + 1):
    if text[i:i + pattern_length] == pattern:
        print(f"Pattern '{pattern}' found at index {i}")
        break
else:
    print(f"Pattern '{pattern}' not found in the text")
