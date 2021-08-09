import plotly.graph_objects as go

# Loop through all the data and print each row.

open_file = open("CupcakeInvoices.csv")
for row in open_file:
    print(row)

# Loop through all the data and princt the type of cupcakes purchased.

open_file = open("CupcakeInvoices.csv")

cupcake_a = "Chocolate"
cupcake_b = "Vanilla"
cupcake_c = "Strawberry"

for x in open_file:
  # x = x.rstrip('\n').split(',')
  
  for value in x:
    if value == 'Chocolate':
      cupcake_a += 1
    elif value == 'Vanilla':
      cupcake_b += 1
    elif value == 'Strawberry':
      cupcake_c += 1

# print(cupcake_a)
# print(cupcake_b)
# print(cupcake_c)

# 5.


# In order to convert to float you need to identify the value that is a float
# Make sure to remember that integer = int (only)

for row in open_file:
    value = row.split(',')
    total = int(value[3]) * float(value[4])
    print(total)

#  6.

for row in open_file:
    value = row.split(',')
    total = total + int(value[3]) * float(value[4])


# Going Further

# Graphing Tools

# import plotly.graph_objects as go
# fig = go.Figure(
#     total = total + ,
#     layout_title_text="A Figure Displayed with fig.show()"
# )
# fig.show()
# I tried. 
