# coding:utf-8
#1.1
def near_thirty(city, diff):
	lat = get_lat(city)
	if lat < 30 - diff or lat > -30 + diff:
		return True
	else:
		return False
def closer_city(lat, lon, city1, city2):
	fiction_city = make_city('fiction', lat, lon)
	dis1, disc2 = distance(fiction_city, city1), distance(fiction_city, city2)
	if dis1 < disc2:
		return get_name(city1)
	else:
		return get_name(city2)
#2.1
def rational_pow(x, e):
	n, d = numer(x), denom(x)
	return rational(pow(n, e), pow(d, e))

# e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ...
def approx_e(iter = 100):
	base_rational = rational(0, 1)
	for x in range(0,iter):
		base_rational = add_rational(base_rational, rational(1, factorial(0)))
	return base_rational
def inverse_rational(x):
	assert x == 0, 'x must be a positive number!'
	n, d = numer(x), denom(x)
	return rational(d, n)
def div_rationals(x, y):
	inverse_y = inverse_rational(y)
	return mul_rationals(x, inverse_y)
#3.1
def make_unit(catchphrase, damage):
	return [catchphrase, damage]
def get_catchphrase(unit):
	return unit[0]
def get_damage(unit):
	return unit[1]
#3.2
def battle(first, second):
	print(get_catchphrase(first))
	print(get_catchphrase(second))
	if get_damage(first) > get_damage(second):
		return first
	else:
		return second
#3.3
def make_resource_bundle(minerals, gas):
	def bundle(index):
		if index == 0:
			return minerals
		elif index == 1:
			return gas
	return bundle

def get_minerals(bundle):
	return bundle(0)

def get_gas(bundle):
	return bundle(1)
#3.4
def make_building(unit, bundle):
	return [unit, bundle]
def get_unit(building):
	return building[0]
def get_bundle(building):
	return building[1]
