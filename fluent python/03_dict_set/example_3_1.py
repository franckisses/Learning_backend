
DIAL_CODES = [
    (86, 'china'),
    (91, 'india'),
    (1 , 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]

country_code = {country:code for code,country in DIAL_CODES}
print(country_code)

filter_country = {code:country for country,code in country_code.items() if code>66}

print(filter_country)
