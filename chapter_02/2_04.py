colors = ['black', 'white']
sizes = ['S', 'M', 'L']
t_shirts = [(color, size) for color in colors
                          for size in sizes]
print(t_shirts)

t_shirts_2 = [(color, size) for size in sizes
                            for color in colors]
print(t_shirts_2)