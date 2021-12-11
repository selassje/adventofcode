char_to_score = {}
char_to_score[")"] = 3
char_to_score["]"] = 57
char_to_score["}"] = 1197
char_to_score[">"] = 25137

opposite_char = {"(": ")", "[": "]", "{": "}", "<": ">"}
opposite_char.update({v: k for k, v in opposite_char.items()})
f = open("input.txt")
syntax_error_code = 0
for i, line in enumerate(f.readlines()):
    line = line.strip()
    expected_closing_chars = []
    for j, c in enumerate(line):
        if c in "([{<":
            expected_closing_chars.append(opposite_char[c])
        if c in ")]}>":
            if c != expected_closing_chars[-1]:
                syntax_error_code += char_to_score[c]
                break
            expected_closing_chars.pop()

print(syntax_error_code)
