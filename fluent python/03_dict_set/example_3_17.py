
dial_codes = [                                            
    (880, 'Bangladesh'),
    (55,  'Brazil'),
    (86,  'China'),
    (91,  'India'),
    (62,  'Indonesia'),
    (81,  'Japan'),
    (234, 'Nigeria'),
    (92,  'Pakistan'),
    (7,   'Russia'),
    (1,   'United States'),
]
d1  = dict(dial_codes)

print('d1', d1.keys())

d2 = dict(sorted(dial_codes))

print('d2', d2.keys())

d3 = dict(sorted(dial_codes, key=lambda x:x[1]))
print('d3', d3.keys())

assert d1 == d2 and d2 == d3
