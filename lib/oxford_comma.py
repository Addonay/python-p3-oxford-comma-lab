def oxford_comma(items):
    if len(items) <= 2:
        return " and ".join(items)
    else:
        last_element = "and " + items[-1]
        other_items = ", ".join(items[:-1])
        return other_items + ", " + last_element
items = ["fiddleheads", "okra", "kohlrabi"]
print(oxford_comma(items))