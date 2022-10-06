# in one late night during October, your friend, who is a math teacher, gave you a list of marks. He knows that you are a hacker, so he told you to:

# Calculate the average mark of the whole class and round it to 3 decimal places.
# Make a dictionary / hash with keys 'h', 'a', and 'l'. To make it clear how many high, average, and low marks they got. High marks are 10 & 9, average marks are 8 & 7, and the rest are counted as low mark.

# Return a list [class_average, dictionary] if there are different type of marks. Or return [class_Average, dictionary, 'They did well'] if they all the whole class got high marks.

def solve(list):
    data = {
        "h": 0,
        "a": 0,
        "l": 0
    }
    for i in list:
        if i == 9 or i == 10:
            data["h"] += 1
        elif i == 7 or i == 8:
            data["a"] += 1
        else:
            data["l"] += 1
    avg = sum(list) / len(list)
    avg = format(avg)
    if avg[:5] == 0:
        avg = "{:.2}".format(sum(list) / len(list))
    elif avg[:4] == 0:
        avg = "{:.1f}".format(sum(list) / len(list))
    else:
        avg = "{:.3f}".format(sum(list) / len(list))
    res = [avg, data]
    return res
