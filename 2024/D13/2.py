import copy
import re
import math as m

with open("input.txt", "r") as file:
    data = file.read().split("\n\n")

machines = []

for i in range(len(data)):
    machines.append([int(number) for number in re.findall(r"([0-9]+)", data[i])])
    machines[i][4] += 10000000000000
    machines[i][5] += 10000000000000


sum = 0


# For part 2, we need our program to be more efficient

# for machine in machines:

#     print(machine)
#     x_a, y_a, x_b, y_b, x_p, y_p = machine
#     lcm_x = m.lcm(x_a, x_b)
#     lcm_y = m.lcm(y_a, y_b)
#     m_x_a = lcm_x // x_a
#     m_x_b = lcm_x // x_b
#     m_y_a = lcm_y // y_a
#     m_y_b = lcm_y // y_b
#     # m_x_a * x_a = m_x_b * x_b = lcm_x and m_y_a * y_a = m_y_b * y_b = lcm_y
#     factor = x_a / x_b
#     # if factor < 3, we prefer to use B over A when we have the choice. Else, we prefer to use A
#     number_of_lcm_x_packets = x_p // lcm_x  # Number of packets of lcm_x we can have
#     number_of_lcm_y_packets = y_p // lcm_y
#     number_of_lcm_packets = min(number_of_lcm_x_packets, number_of_lcm_y_packets)
#     x_p_rest = x_p - number_of_lcm_packets * lcm_x
#     y_p_rest = y_p - number_of_lcm_packets * lcm_y

#     min_cost = -1

#     if factor >= 3:
#         # We prefer to use A
#         n_a_init = number_of_lcm_x_packets * m_x_a

#         max_a = min(x_p_rest // x_a + 1, y_p_rest // y_a + 1)
#         for n_a_rest in range(max_a, -1, -1):
#             if (
#                 (x_p_rest - n_a_rest * x_a) % x_b == 0
#                 and (y_p_rest - n_a_rest * y_a) % y_b == 0
#                 and (x_p_rest - n_a_rest * x_a) // x_b
#                 == (y_p_rest - n_a_rest * y_a) // y_b
#             ):
#                 n_b = (x_p_rest - n_a_rest * x_a) // x_b
#                 min_cost = 3 * (n_a_init + n_a_rest) + n_b
#                 break

#     else:
#         # We prefer to use B

#         n_b_init = number_of_lcm_packets * m_x_b

#         max_b = min(x_p_rest // x_b + 1, y_p_rest // y_b + 1)
#         for n_b_rest in range(max_b, -1, -1):
#             if (
#                 (x_p_rest - n_b_rest * x_b) % x_a == 0
#                 and (y_p_rest - n_b_rest * y_b) % y_a == 0
#                 and (x_p_rest - n_b_rest * x_b) // x_a
#                 == (y_p_rest - n_b_rest * y_b) // y_a
#             ):
#                 print("slay")
#                 n_a = (x_p_rest - n_b_rest * x_b) // x_a
#                 min_cost = (n_b_init + n_b_rest) + 3 * n_a
#                 break

#     if min_cost != -1:
#         sum += min_cost

# sum


for machine in machines:
    x_a, y_a, x_b, y_b, x_p, y_p = machine
    # There is no "optimal" way to get a prize, there is only one solution, unless A is a multiple of B or vice versa
    lcm_a = m.lcm(y_a, x_a)
    m_x_a = lcm_a // x_a
    m_y_a = lcm_a // y_a
    n_b = (m_x_a * x_p - m_y_a * y_p) // (m_x_a * x_b - m_y_a * y_b)
    n_a = (x_p - n_b * x_b) // x_a
    if (
        n_a >= 0
        and n_b >= 0
        and n_a * x_a + n_b * x_b == x_p
        and n_a * y_a + n_b * y_b == y_p
    ):
        sum += 3 * n_a + n_b
