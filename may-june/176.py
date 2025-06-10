import math
from collections import defaultdict


def convert_to_base_unit(amount, unit):
    if unit == 'kg':
        return amount * 1000, 'g'
    elif unit == 'l':
        return amount * 1000, 'ml'
    elif unit == 'tens':
        return amount * 10, 'cnt'
    else:
        return amount, unit


def normalize_amount(amount, unit, target_unit):
    amount_base, base_unit = convert_to_base_unit(amount, unit)
    target_amount_base, _ = convert_to_base_unit(1, target_unit)
    return amount_base / target_amount_base


n = int(input())
dishes = []
ingredients_per_dish = {}

for _ in range(n):
    parts = input().split()
    dish_name = parts[0]
    c_i = int(parts[1])
    z_i = int(parts[2])
    dishes.append((dish_name, c_i))

    ingredients = []
    for _ in range(z_i):
        ing_parts = input().split()
        a_ij = int(ing_parts[-2])
        u_ij = ing_parts[-1]
        s_ij = ' '.join(ing_parts[:-2])
        ingredients.append((s_ij, a_ij, u_ij))
    ingredients_per_dish[dish_name] = (c_i, ingredients)

k = int(input())
price_catalog = {}

for _ in range(k):
    t_i, p_i, a_i, u_i = input().split()
    p_i = int(p_i)
    a_i = int(a_i)
    price_catalog[t_i] = (p_i, a_i, u_i)

m = int(input())
nutrition_catalog = {}

for _ in range(m):
    parts = input().split()
    t_i = parts[0]
    a_i = int(parts[1])
    u_i = parts[2]
    pr_i = float(parts[3])
    f_i = float(parts[4])
    ch_i = float(parts[5])
    fv_i = float(parts[6])
    nutrition_catalog[t_i] = (a_i, u_i, pr_i, f_i, ch_i, fv_i)

total_ingredients = defaultdict(int)

for dish_name, (c_i, ingredients) in ingredients_per_dish.items():
    for s_ij, a_ij, u_ij in ingredients:
        total_amount_base, _ = convert_to_base_unit(a_ij * c_i, u_ij)
        total_ingredients[s_ij] += total_amount_base

required_packages = defaultdict(int)
total_cost = 0

for t_i, total_amount_base in total_ingredients.items():
    p_i, a_pack, u_pack = price_catalog[t_i]
    pack_amount_base, _ = convert_to_base_unit(a_pack, u_pack)
    num_packs = math.ceil(total_amount_base / pack_amount_base)
    required_packages[t_i] = num_packs
    total_cost += num_packs * p_i

print(total_cost)

for t_i in price_catalog:
    print(t_i, required_packages.get(t_i, 0))

for dish_name, (c_i, ingredients) in ingredients_per_dish.items():
    total_pr = 0.0
    total_f = 0.0
    total_ch = 0.0
    total_fv = 0.0

    for s_ij, a_ij, u_ij in ingredients:
        a_nutr, u_nutr, pr_i, f_i, ch_i, fv_i = nutrition_catalog[s_ij]
        ing_amount_base, _ = convert_to_base_unit(a_ij, u_ij)
        nutr_amount_base, _ = convert_to_base_unit(a_nutr, u_nutr)

        ratio = ing_amount_base / nutr_amount_base
        total_pr += pr_i * ratio
        total_f += f_i * ratio
        total_ch += ch_i * ratio
        total_fv += fv_i * ratio

    print(f"{dish_name} {round(total_pr, 3)} {round(total_f, 3)} {round(total_ch, 3)} {round(total_fv, 3)}")

