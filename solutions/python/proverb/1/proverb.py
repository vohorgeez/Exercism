def proverb(*input_data, qualifier=None):
    output = []
    if len(input_data) != 0:
        for i in range(len(input_data)-1):
            output.append(f"For want of a {input_data[i]} the {input_data[i+1]} was lost.")
        output.append(f"And all for the want of a {qualifier+" " if qualifier is not None else ""}{input_data[0]}.")
    return output