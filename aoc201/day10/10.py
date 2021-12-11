closing_char_to_syntax_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
closing_char_to_completion_score = {")": 1, "]": 2, "}": 3, ">": 4}

opposite_char = {"(": ")", "[": "]", "{": "}", "<": ">"}
opposite_char.update({v: k for k, v in opposite_char.items()})
f = open("input.txt")
syntax_error_code = 0
completion_scores = []

for line in f.readlines():
    line = line.strip()
    expected_closing_chars = []
    for c in line:
        if c in "([{<":
            expected_closing_chars.append(opposite_char[c])
        else:
            expected = expected_closing_chars.pop()
            if c != expected:
                syntax_error_code += closing_char_to_syntax_score[c]
                expected_closing_chars.clear()
                break
    if len(expected_closing_chars) != 0:
        completion_score = 0
        expected_closing_chars.reverse()
        for (i, c) in enumerate(expected_closing_chars):
            completion_score = (
                completion_score * 5 + closing_char_to_completion_score[c]
            )
        completion_scores.append(completion_score)

print(syntax_error_code)

completion_scores.sort()
middle_completion_score = completion_scores[int(len(completion_scores) / 2)]
print(middle_completion_score)
