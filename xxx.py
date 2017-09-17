import xlsxwriter
import scipy.misc as smc

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Workbook1.xlsx')
keno = workbook.add_worksheet('Keno')
# Some data we want to write to the worksheet.
#expenses = (
#    ['Rent', 1000],
#    ['Gas',   100],
#    ['Food',  300],
#    ['Gym',    50],
#)
spot = []
catch = []
combin = []
count = 0
spotcomb = []
prob = []
for x in range(1, 16):
    curcomb = 0
    for y in range(0, x+1):
        spot.append(x)  # spot is the number of numbers betting on.
        catch.append(y)  # catch is the number of numbers correct.
        z = smc.comb(20, y)*smc.comb(60, x-y)
        combin.append(z)  # combin is the combinatorials of the catch.
        curcomb += z
        count += 1
    spotcomb.append(curcomb)  # spotcomb is the combinatorials of the spot (sum of catches)

x = 0
ct = 2
for m in range(0, count+1):
    prob.append(combin[m]/spotcomb[x])  # prob is the probability of each combin in spotcomb
    if m == x+ct:
        x += 1
        ct += 1

# print(combin)



price = [0, 3, 0, 0, 12, 0, 0, 1, 44, 0, 0, 0, 2, 20, 522, 0, 0, 0, 1, 5, 83, 1660, 0, 0, 0, 1, 2, 14, 153, 5000, 0, 0,
         0, 0, 2, 7, 50, 840, 20000, 0, 0, 0, 0, 1, 2, 20, 155, 1000, 250000, 1, 0, 0, 0, 0, 1, 20, 150, 950, 7000,
         50000, 0, 1, 0, 0, 0, 1, 5, 35, 260, 2500, 22000, 100000, 4, 1, 0, 0, 0, 1, 4, 15, 80, 610, 7000, 70000,
         140000, 5, 1, 0, 0, 0, 1, 2, 8, 45, 350, 2000, 10000, 80000, 160000, 7, 1, 0, 0, 0, 0, 1, 7, 35, 220, 1000,
         8500, 25000, 90000, 100000, 15, 2, 0, 0, 0, 0, 1, 5, 15, 50, 350, 3000, 20000, 50000, 100000, 200000]


# KEY PART:
# basically need to look at profit for multi bets (4x1, 4x2, 4x3?, 1x4) at scale
# compensatory overlay. Use each to build up a proportion of returns, split bet

def combo_checker(spot_list, quant_list):  # assume_max_overlap = 1  # need to include ability to spread

    for spot in spot_list:


# better version / different:
# ideally, input all numbers for all spots and get an average outcome
def input_output_all(num_list_spot_list, pay_list):  # len(pay_list) == len(spot_list) need to check
    for spot in num_list_spot_list:
        for num in spot:

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
#for item, cost in (expenses):
    #worksheet.write(row, col,     item)
    #worksheet.write(row, col + 1, cost)
    #row += 1
'''
for p in price:
    keno.write(row, col, spot)
    keno.write(row, col+1, catch)
    keno.write(row, col+2, price)
    keno.write(row, col+3, combin)
    keno.write(row, col+4, prob)
    keno.write(row, col+5, return)

    row += 1
'''
# Write a total using a formula.
#worksheet.write(row, 0, 'Total')
#worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()