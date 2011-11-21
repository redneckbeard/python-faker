import random

from faker.generators.name import first_name, last_name
from faker.generators.utils import numerify, letterify, bothify


def zip_code():
    return numerify(random.choice(['#####', '#####-####']))

def us_state():
    return random.choice([
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
        'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
        'West Virginia', 'Wisconsin', 'Wyoming'
    ])

def us_state_abbr():
    return random.choice("""AL AK AS AZ AR CA CO CT DE DC FM FL GA GU HI ID IL
    IN IA KS KY LA ME MH MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND MP OH OK
    OR PW PA PR RI SC SD TN TX UT VT VI VA WA WV WI WY AE AA AP""".split())

def city_prefix():
    return random.choice('North East West South New Lake Port'.split())

def city_suffix():
    return random.choice("""town ton land ville berg burgh borough bury view
    port mouth stad furt chester mouth fort haven side shire""".split())

def city():
    return random.choice([
        '%s %s%s' % (city_prefix(), first_name(), city_suffix()),
        '%s %s' % (city_prefix(), first_name()),
        '%s%s' % (first_name(), city_suffix()),
        '%s%s' % (last_name(), city_suffix()),
    ])

def street_suffix():
    return random.choice("""Alley Avenue Branch Bridge Brook Brooks Burg Burgs
        Bypass Camp Canyon Cape Causeway Center Centers Circle Circles Cliff
        Cliffs Club Common Corner Corners Course Court Courts Cove Coves Creek
        Crescent Crest Crossing Crossroad Curve Dale Dam Divide Drive Drive
        Drives Estate Estates Expressway Extension Extensions Fall Falls Ferry
        Field Fields Flat Flats Ford Fords Forest Forge Forges Fork Forks Fort
        Freeway Garden Gardens Gateway Glen Glens Green Greens Grove Groves
        Harbor Harbors Haven Heights Highway Hill Hills Hollow Inlet Inlet
        Island Island Islands Islands Isle Isle Junction Junctions Key Keys
        Knoll Knolls Lake Lakes Land Landing Lane Light Lights Loaf Lock Locks
        Locks Lodge Lodge Loop Mall Manor Manors Meadow Meadows Mews Mill Mills
        Mission Mission Motorway Mount Mountain Mountain Mountains Mountains
        Neck Orchard Oval Overpass Park Parks Parkway Parkways Pass Passage
        Path Pike Pine Pines Place Plain Plains Plains Plaza Plaza Point
        Points Port Port Ports Ports Prairie Prairie Radial Ramp Ranch Rapid
        Rapids Rest Ridge Ridges River Road Road Roads Roads Route Row Rue Run
        Shoal Shoals Shore Shores Skyway Spring Springs Springs Spur Spurs
        Square Square Squares Squares Station Station Stravenue Stravenue
        Stream Stream Street Street Streets Summit Summit Terrace Throughway
        Trace Track Trafficway Trail Trail Tunnel Tunnel Turnpike Turnpike
        Underpass Union Unions Valley Valleys Via Viaduct View Views Village
        Village  Villages Ville Vista Vista Walk Walks Wall Way Ways
        Well Wells""".split())

def street_name():
    return random.choice([
        ' '.join([last_name(), street_suffix()]),
        ' '.join([first_name(), street_suffix()])
    ])

def street_address(include_secondary=False):
    addr = numerify(random.choice([
        '##### %s' % street_name(),
        '#### %s' % street_name(),
        '### %s' % street_name()
    ]))
    if include_secondary:
        addr = ' '.join([addr, secondary_address()])
    return addr

def secondary_address():
    return numerify(random.choice([
      'Apt. ###',
      'Suite ###'
    ]))

# UK Variants
def uk_county():
    return random.choice([
        'Avon', 'Bedfordshire', 'Berkshire', 'Borders', 'Buckinghamshire',
        'Cambridgeshire', 'Central', 'Cheshire', 'Cleveland', 'Clwyd',
        'Cornwall', 'County Antrim', 'County Armagh', 'County Down',
        'County Fermanagh', 'County Londonderry', 'County Tyrone', 'Cumbria',
        'Derbyshire', 'Devon', 'Dorset', 'Dumfries and Galloway', 'Durham',
        'Dyfed', 'East Sussex', 'Essex', 'Fife', 'Gloucestershire', 'Grampian',
        'Greater Manchester', 'Gwent', 'Gwynedd County', 'Hampshire',
        'Herefordshire', 'Hertfordshire', 'Highlands and Islands', 'Humberside',
        'Isle of Wight', 'Kent', 'Lancashire', 'Leicestershire', 'Lincolnshire',
        'Lothian', 'Merseyside', 'Mid Glamorgan', 'Norfolk', 'North Yorkshire',
        'Northamptonshire', 'Northumberland', 'Nottinghamshire', 'Oxfordshire',
        'Powys', 'Rutland', 'Shropshire', 'Somerset', 'South Glamorgan',
        'South Yorkshire', 'Staffordshire', 'Strathclyde', 'Suffolk', 'Surrey',
        'Tayside', 'Tyne and Wear', 'Warwickshire', 'West Glamorgan',
        'West Midlands', 'West Sussex', 'West Yorkshire', 'Wiltshire',
        'Worcestershire'
    ])

def uk_country():
    return random.choice(['England', 'Scotland', 'Wales', 'Northern Ireland'])

def uk_postcode():
    return bothify(random.choice([
      '??# #??',
      '??## #??'
    ])).upper()

# Canadian variants
def ca_province():
    """Includes the ten Canadian Provinces as well as the
    three Canadian Territories.
    """
    return random.choice(['Alberta',
                        'British Columbia',
                        'Manitoba',
                        'New Brunswick',
                        'Newfoundland and Labrador',
                        'Northwest Territories',
                        'Nova Scotia',
                        'Nunavut',
                        'Ontario',
                        'Prince Edward Island',
                        'Quebec',
                        'Saskatchewan',
                        'Yukon',
                        ])

def ca_province_abbr():
    """Postal abbreviations for the ten Canadian Provinces as
    well as the three Canadian Territories.
    """
    return random.choice(['AB', 'BC', 'MB', 'NB', 'NL', 'NS',
                          'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT'])

def ca_postal_code():
    """Returns a randomly-generated postal code in the
    Canadian format
    """
    return bothify('?#? #?#').upper()
