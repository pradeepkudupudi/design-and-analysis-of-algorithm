words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

res = []  # To store the final list of lines
current_line = []  # Current line of words
current_len = 0  # Current length of words in the line (excluding spaces)

for word in words:
    # If adding this word exceeds the maxWidth, we need to process the current line
    if current_len + len(word) + len(current_line) > maxWidth:
        # Distribute spaces evenly
        if len(current_line) == 1:  # If only one word in the line, just add spaces at the end
            res.append(current_line[0] + ' ' * (maxWidth - len(current_line[0])))
        else:
            total_spaces = maxWidth - current_len  # Total spaces to distribute
            even_spaces = total_spaces // (len(current_line) - 1)  # Spaces between words
            extra_spaces = total_spaces % (len(current_line) - 1)  # Extra spaces for left side
            
            line = current_line[0]
            for i in range(1, len(current_line)):
                # Add spaces between words
                line += ' ' * (even_spaces + (1 if i <= extra_spaces else 0)) + current_line[i]
            res.append(line)
        
        # Reset for the next line
        current_line = [word]
        current_len = len(word)
    else:
        # Add the word to the current line
        current_line.append(word)
        current_len += len(word)

# Last line should be left-justified
last_line = ' '.join(current_line)
res.append(last_line + ' ' * (maxWidth - len(last_line)))

# Output the final result
print(res)
