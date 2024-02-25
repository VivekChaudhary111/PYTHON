def lastRemainingColor(colors):
    while len(colors) > 1:
        for i in range(len(colors) - 1):
            if colors[i] != colors[i + 1]:
                if (colors[i] == "R" and colors[i + 1] == "G") or (colors[i] == "G" and colors[i + 1] == "R"):
                    colors[i:i + 2] = "B"
                elif (colors[i] == "R" and colors[i + 1] == "B") or (colors[i] == "B" and colors[i + 1] == "R"):
                    colors[i:i + 2] = "G"
                elif (colors[i] == "G" and colors[i + 1] == "B") or (colors[i] == "B" and colors[i + 1] == "G"):
                    colors[i:i + 2] = "R"
                break

    return colors

# Example usage:
initial_colors = ["R", "G", "B", "R", "G"]
result = lastRemainingColor(initial_colors)
print(result)  # The result will be the last remaining color.
