"""Defines constants for the Two Point Science package.

Defines types and values used by the entire package.

    Typical usage example:

    from tps.tph_constants import (TPH_ROOM_DICT, TPH_ROOM_LIST)
"""

# Standard
from collections import namedtuple

# Third Party

# Local
from tps.menu import Menu


# 1. DATA TYPES
HospitalDetails = namedtuple('HospitalDetails', 'illness')
IllnessDetails = namedtuple('IllnessDetails', 'diagnostic treatment')
RoomDetails = namedtuple('RoomDetails', 'purpose')

# 2. MACROS

# DISEASE NAMES
# NOTE: Disease macro names were truncated to represent the acronym (for names with more than
#   one word) or just enough letters of the name to be unique (min: 2).
TPH_NAME_DISEASE_BE = 'Beheadedness'
TPH_NAME_DISEASE_BOA = 'Bloat of Arms'
TPH_NAME_DISEASE_BP = 'Bionic Plague'
TPH_NAME_DISEASE_BY = 'Byteheadedness'
TPH_NAME_DISEASE_CAR = 'Chewed a Rose'
TPH_NAME_DISEASE_FU = 'Futurism'
TPH_NAME_DISEASE_JRI = 'Jester Infection'
TPH_NAME_DISEASE_GD = 'Glass Dome'
TPH_NAME_DISEASE_HC = 'Hacking Cough'
TPH_NAME_DISEASE_HL = 'Historical Laughter'
TPH_NAME_DISEASE_HOL = 'Hologlands'
TPH_NAME_DISEASE_HOT = 'Hotheadedness'
TPH_NAME_DISEASE_PM = 'Premature Mummification'
TPH_NAME_DISEASE_PT = 'Pneumatic Tubes'
TPH_NAME_DISEASE_VD = 'Verbal Diarrhoea'

# HOSPITAL NAMES
# NOTE: Hospital macro names were truncated to represent the acronym (for names with more than
#   one word) or just enough letters of the name to be unique (min: 2).
TPH_NAME_HOSPITAL_BL = 'Blighton'
TPH_NAME_HOSPITAL_CF = 'Camouflage Falls'
TPH_NAME_HOSPITAL_C24 = 'Chasm 24'
TPH_NAME_HOSPITAL_CAT = 'Clockwise-above-Thyme'
TPH_NAME_HOSPITAL_CBT = 'Clockwise-before-Thyme'
TPH_NAME_HOSPITAL_CUT = 'Clockwise-upon-Thyme'
TPH_NAME_HOSPITAL_CR = 'Croquembouche'
TPH_NAME_HOSPITAL_DUB = 'Duckworth-upon-Bilge'
TPH_NAME_HOSPITAL_FA = 'Fitzpocket Academy'
TPH_NAME_HOSPITAL_FLE = 'Flemington'
TPH_NAME_HOSPITAL_FLO = 'Flottering'
TPH_NAME_HOSPITAL_GO = 'Goldpan'
TPH_NAME_HOSPITAL_GB = 'Grockle Bay'
TPH_NAME_HOSPITAL_HO = 'Hogsport'
TPH_NAME_HOSPITAL_LB = 'Lower Bullocks'
TPH_NAME_HOSPITAL_MD = 'Melt Downs'
TPH_NAME_HOSPITAL_MU = 'Mitton University'
TPH_NAME_HOSPITAL_MF = 'Mudbury Festival'
TPH_NAME_HOSPITAL_ON = 'Old Newpoint'
TPH_NAME_HOSPITAL_OV = 'Overgrowth'
TPH_NAME_HOSPITAL_PR = 'Pebberley Reef'
TPH_NAME_HOSPITAL_PW = 'Pelican Wharf'
TPH_NAME_HOSPITAL_PS = 'Plywood Studios'
TPH_NAME_HOSPITAL_RC = 'Roquefort Castle'
TPH_NAME_HOSPITAL_RH = 'Rotting Hill'
TPH_NAME_HOSPITAL_SM = 'Smogley'
TPH_NAME_HOSPITAL_SP = 'Sweaty Palms'
TPH_NAME_HOSPITAL_SW = 'Swelbard'
TPH_NAME_HOSPITAL_TM = 'Topless Mountain'
TPH_NAME_HOSPITAL_TU = 'Tumble'
TPH_NAME_HOSPITAL_UH = 'Underlook Hotel'
TPH_NAME_HOSPITAL_WA = 'Wanderoff'
TPH_NAME_HOSPITAL_WI = 'Windsock'

# ROOM NAMES
TPH_NAME_ROOM_GP = "GP's Office"
TPH_NAME_ROOM_CR = 'Cryptology'

TPH_ROOM_DICT = {
    'Cardiology': RoomDetails(purpose='Diagnostic'),
    'Chromatherapy': RoomDetails(purpose='Treatment'),
    'Clown Clinic': RoomDetails(purpose='Treatment'),
    TPH_NAME_ROOM_CR: RoomDetails(purpose='Treatment'),
    'De-Lux Clinic': RoomDetails(purpose='Treatment'),
    'DNA Lab': RoomDetails(purpose='Both'),
    'Fluid Analysis': RoomDetails(purpose='Diagnostic'),
    'Fracture Ward': RoomDetails(purpose='Treatment'),
    'General Diagnosis': RoomDetails(purpose='Diagnostic'),
    TPH_NAME_ROOM_GP: RoomDetails(purpose='Diagnostic'),
    'Head Office': RoomDetails(purpose='Treatment'),
    'Injection Room': RoomDetails(purpose='Treatment'),
    'M.E.G.A Scan': RoomDetails(purpose='Diagnostic'),
    'Pans Lab': RoomDetails(purpose='Treatment'),
    'Pest Control': RoomDetails(purpose='Treatment'),
    'Pharmacy': RoomDetails(purpose='Treatment'),
    'Psychiatry': RoomDetails(purpose='Both'),
    'Recurvery Room': RoomDetails(purpose='Treatment'),
    'Resolution Lab': RoomDetails(purpose='Treatment'),
    'Shock Clinic': RoomDetails(purpose='Treatment'),
    'Surgery': RoomDetails(purpose='Treatment'),
    'Ward': RoomDetails(purpose='Both'),
    'X-Ray': RoomDetails(purpose='Diagnostic'),
}

TPH_ROOM_LIST = list(TPH_ROOM_DICT.keys())

TPH_DIAGNOSTIC_LIST = [room for room, value in TPH_ROOM_DICT.items()
                       if value.purpose in ['Diagnostic', 'Both']]

TPH_TREATMENT_LIST = [room for room, value in TPH_ROOM_DICT.items()
                      if value.purpose in ['Treatment', 'Both']]

TPH_DUAL_PURPOSE_LIST = [room for room, value in TPH_ROOM_DICT.items() if value.purpose == 'Both']

TPH_HOSPITAL_DICT = {
    TPH_NAME_HOSPITAL_BL:
    HospitalDetails(illness=['8-bitten', 'Animal Magnetism', 'Cubism', 'Decision Rash',
                             'Emperor Complex', 'Freudian Lips', 'Grey Anatomy', 'Gurning Loins',
                             'Heart Throb', 'Leopard Skin', 'Litter Bug', 'Lycanthropy',
                             'Mime Crisis', 'Misery Guts', 'Mock Star', 'Mood Poisoning',
                             'Night Fever', 'Potty Mouth', TPH_NAME_DISEASE_PM, 'Pudding Blood',
                             'Rock Bottom', 'Shock Horror', 'Spinal Bap', 'Spontaneous Combustion',
                             'Touch of Midas', 'Turtle Head', TPH_NAME_DISEASE_VD]),
    'Camouflage Falls': HospitalDetails(illness=[]),
    'Chasm 24': HospitalDetails(illness=[]),
    TPH_NAME_HOSPITAL_CAT:
    HospitalDetails(illness=['Jest Infection', TPH_NAME_DISEASE_JRI, TPH_NAME_DISEASE_BE,
                             TPH_NAME_DISEASE_BY, TPH_NAME_DISEASE_HOT, 'Lightheadedness', 'Fossil Eyes',
                             'Jumbo DNA', 'Time Warts', 'Woolly Man-Mouth', 'Clockjaw',
                             'Fractured Timeline', TPH_NAME_DISEASE_GD, 'Missing Link',
                             TPH_NAME_DISEASE_BOA, 'Dino Sores', TPH_NAME_DISEASE_HC, 'Pudding Blood',
                             TPH_NAME_DISEASE_CAR, 'Cod Piece', TPH_NAME_DISEASE_HOL, 'Misery Guts', 'Parapox',
                             'Artificial Intelligence', 'Fomo Sapiens', TPH_NAME_DISEASE_HL,
                             'Reptile Dysfunction', 'Cubism', TPH_NAME_DISEASE_FU, TPH_NAME_DISEASE_BP,
                             'Bone Head', 'Rolling Stones', 'Loopy', 'Monobrow', TPH_NAME_DISEASE_PT,
                             'Predestinitis']),
    'Clockwise-before-Thyme': HospitalDetails(illness=[]),
    'Clockwise-upon-Thyme': HospitalDetails(illness=[]),
    'Croquembouche': HospitalDetails(illness=[]),
    'Duckworth-upon-Bilge': HospitalDetails(illness=[]),
    'Fitzpocket Academy': HospitalDetails(illness=[]),
    'Flemington': HospitalDetails(illness=[]),
    'Flottering': HospitalDetails(illness=[]),
    'Goldpan': HospitalDetails(illness=[]),
    # https://two-point-hospital.fandom.com/wiki/Grockle_Bay
    # TPH_NAME_HOSPITAL_GB:
    # HospitalDetails(illness=['Denim Genes', 'Leopard Skin', 'Touch of Midas', 'Broken Face',
    #                          'Hurty Leg', 'Shattered', 'Turtle Head', 'Pudding Blood',
    #                          'Rock Bottom', 'Spontaneous Combustion', 'Misery Guts',
    #                          TPH_NAME_DISEASE_VD, 'Emperor Complex', 'Inflated Ego', 'Mime Crisis',
    #                          'Cubism', '8-bitten', 'Shock Horror', 'Floppy Discs', 'Heart Throb',
    #                          'Gurning Loins', 'Jazz Hand', 'Lazy Bones', 'Mucky Feet']),
    # Observed in game (see: res/Grockle_Bay-Illness_List-?.png)
    TPH_NAME_HOSPITAL_GB:
    HospitalDetails(illness=[TPH_NAME_DISEASE_VD, 'Lazy Bones', 'Misery Guts', 'Mucky Feet',
                             'Mime Crisis', 'Cubism', 'Inflated Ego', 'Jazz Hand', 'Rock Bottom',
                             'Hurty Leg', 'Broken Face', '8-bitten', 'Floppy Discs',
                             'Emperor Complex', 'Denim Genes', 'Turtle Head', 'Shock Horror',
                             'Pudding Blood', 'Leopard Skin', 'Heart Throb', 'Shattered',
                             'Spontaneous Combustion', 'Jumbo DNA', 'Gurning Loins',
                             'Touch of Midas']),
    'Hogsport': HospitalDetails(illness=[]),
    'Lower Bullocks': HospitalDetails(illness=[]),
    'Melt Downs': HospitalDetails(illness=[]),
    # Observed in game (see: res/Mitton_University-Illness_List-?.png)
    TPH_NAME_HOSPITAL_MU:
    HospitalDetails(illness=['Bogwarts', 'Misery Guts', 'Lazy Bones', 'Grey Anatomy',
                             'Lightheadedness', 'Mucky Feet', 'Potty Mouth', 'Jest Infection',
                             'Mock Star', 'Night Fever', 'Freudian Lips', 'Inflated Ego',
                             'Mood Poisoning', 'Rock Bottom', 'Lycanthropy', 'Decision Rash',
                             'Boggled Mind', 'Headcrabedness']),
    'Mudbury Festival': HospitalDetails(illness=[]),
    'Old Newpoint': HospitalDetails(illness=[]),
    'Overgrowth': HospitalDetails(illness=[]),
    'Pebberley Reef': HospitalDetails(illness=[]),
    'Pelican Wharf': HospitalDetails(illness=[]),
    'Plywood Studios': HospitalDetails(illness=[]),
    'Roquefort Castle': HospitalDetails(illness=[]),
    'Rotting Hill': HospitalDetails(illness=[]),
    TPH_NAME_HOSPITAL_SM:
    HospitalDetails(illness=['Grey Anatomy', 'Cross Bones', 'Humerus Injury', 'Hurty Leg',
                             'Turtle Head', 'Decision Rash', 'Mood Poisoning',
                             'Spontaneous Combustion', 'Pandemic', 'Animal Magnetism',
                             'Floppy Discs', 'Gurning Loins', 'Heart Throb', 'Pipe Organs',
                             'Spinal Bap', 'Bed Face', 'Jazz Hand', 'Portishead']),
    'Sweaty Palms': HospitalDetails(illness=[]),
    'Swelbard': HospitalDetails(illness=[]),
    'Topless Mountain': HospitalDetails(illness=[]),
    'Tumble': HospitalDetails(illness=[]),
    'Underlook Hotel': HospitalDetails(illness=[]),
    'Wanderoff': HospitalDetails(illness=[]),
    'Windsock': HospitalDetails(illness=[]),
}

TPH_HOSPITAL_LIST = list(TPH_HOSPITAL_DICT.keys())

TPH_ILLNESS_DICT = {
    '8-bitten': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'],
                               treatment='Resolution Lab'),
    'Animal Magnetism': IllnessDetails(diagnostic=['Cardiology', 'M.E.G.A Scan'],
                                       treatment='Pest Control'),
    'Artificial Intelligence': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'Ward'],
                                              treatment='Psychiatry'),
    'Bed Face': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Ward'),
    TPH_NAME_DISEASE_BE: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='De-Lux Clinic'),
    TPH_NAME_DISEASE_BP: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'Cardiology'],
                                        treatment='Surgery'),
    TPH_NAME_DISEASE_BOA: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Injection Room'),
    TPH_NAME_DISEASE_BY: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='De-Lux Clinic'),
    'Boggled Mind': IllnessDetails(diagnostic=['Ward', 'X-Ray'], treatment='Psychiatry'),
    'Bogwarts': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'],
                               treatment='Pharmacy'),
    'Bone Head': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Surgery'),
    'Broken Face': IllnessDetails(diagnostic=['Cardiology', 'Fluid Analysis'],
                                  treatment='Fracture Ward'),
    TPH_NAME_DISEASE_CAR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Clamp': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Clockjaw': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Fracture Ward'),
    'Cod Piece': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Cross Bones': IllnessDetails(diagnostic=['Psychiatry', 'X-Ray'], treatment='Fracture Ward'),
    'Cubism': IllnessDetails(diagnostic=['Fluid Analysis', 'X-Ray'], treatment='Recurvery Room'),
    'Decision Rash': IllnessDetails(diagnostic=['Fluid Analysis', 'Cardiology'],
                                    treatment='Injection Room'),
    'Denim Genes': IllnessDetails(diagnostic=['Fluid Analysis', 'M.E.G.A Scan'],
                                  treatment='DNA Lab'),
    'Dino Sores': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Injection Room'),
    'Emperor Complex': IllnessDetails(diagnostic=['DNA Lab', 'Cardiology'],
                                      treatment='Psychiatry'),
    'Floppy Discs': IllnessDetails(diagnostic=['X-Ray', 'M.E.G.A Scan'], treatment='Surgery'),
    'Flumps': IllnessDetails(diagnostic=['Cardiology', 'M.E.G.A Scan'], treatment='DNA Lab'),
    'Fomo Sapiens': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Forefraught': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Fossil Eyes': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'DNA Lab'], treatment='DNA Lab'),
    'Fractured Timeline': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Fracture Ward'),
    'Freudian Lips': IllnessDetails(diagnostic=['Cardiology', 'Psychiatry'],
                                    treatment='Psychiatry'),
    TPH_NAME_DISEASE_FU: IllnessDetails(diagnostic=['DNA Lab', 'X-Ray'],
                                        treatment='Recurvery Room'),
    'Grey Anatomy': IllnessDetails(diagnostic=['Fluid Analysis', 'M.E.G.A Scan'],
                                   treatment='Chromatherapy'),
    TPH_NAME_DISEASE_GD: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'Ward'],
                                        treatment='Fracture Ward'),
    'Grout': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Gurning Loins': IllnessDetails(diagnostic=['General Diagnosis', 'M.E.G.A Scan'],
                                    treatment='Surgery'),
    TPH_NAME_DISEASE_HC: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Injection Room'),
    'Headcrabedness': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='De-Lux Clinic'),
    'Heart Throb': IllnessDetails(diagnostic=['Cardiology', 'Fluid Analysis'],
                                  treatment='Surgery'),
    TPH_NAME_DISEASE_HL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    TPH_NAME_DISEASE_HOL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'X-Ray'], treatment='Pharmacy'),
    TPH_NAME_DISEASE_HOT: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='De-Lux Clinic'),
    'Humerus Injury': IllnessDetails(diagnostic=['General Diagnosis', 'Ward'],
                                     treatment='Fracture Ward'),
    'Hurty Leg': IllnessDetails(diagnostic=['General Diagnosis', 'X-Ray'],
                                treatment='Fracture Ward'),
    'Inflated Ego': IllnessDetails(diagnostic=['Fluid Analysis', 'General Diagnosis'],
                                   treatment='Psychiatry'),
    'Jazz Hand': IllnessDetails(diagnostic=['X-Ray', 'M.E.G.A Scan'], treatment='Ward'),
    'Jest Infection': IllnessDetails(diagnostic=['Psychiatry', 'X-Ray'], treatment='Clown Clinic'),
    TPH_NAME_DISEASE_JRI: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Clown Clinic'),
    'Jumbo DNA': IllnessDetails(diagnostic=['M.E.G.A Scan', 'Fluid Analysis'],
                                treatment='DNA Lab'),
    'Lazy Bones': IllnessDetails(diagnostic=['Cardiology', 'General Diagnosis'],
                                 treatment='Ward'),
    'Leopard Skin': IllnessDetails(diagnostic=['Fluid Analysis', 'X-Ray'],
                                   treatment='DNA Lab'),
    'Lightheadedness': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'],
                                      treatment='De-Lux Clinic'),
    'Lightheadedness (Frightheadedness)': IllnessDetails(diagnostic=['', ''],
                                                         treatment='De-Lux Clinic'),
    'Litter Bug': IllnessDetails(diagnostic=['Fluid Analysis', 'X-Ray'],
                                 treatment='Injection Room'),
    'Loopy': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    'Lycanthropy': IllnessDetails(diagnostic=['Cardiology', 'Fluid Analysis'],
                                  treatment='Pharmacy'),
    'Mime Crisis': IllnessDetails(diagnostic=['Cardiology', 'Psychiatry'], treatment='Psychiatry'),
    'Misery Guts': IllnessDetails(diagnostic=['Cardiology', 'Fluid Analysis'],
                                  treatment='Pharmacy'),
    'Missing Link': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'M.E.G.A Scan'],
                                   treatment='Fracture Ward'),
    'Mock Star': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'],
                                treatment='Psychiatry'),
    'Monobrow': IllnessDetails(diagnostic=['Ward', 'X-Ray'], treatment='Ward'),
    'Mood Poisoning': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'],
                                     treatment='Injection Room'),
    'Mucky Feet': IllnessDetails(diagnostic=['DNA Lab', 'X-Ray'], treatment='Ward'),
    'Night Fever': IllnessDetails(diagnostic=['General Diagnosis', 'Psychiatry'],
                                  treatment='Psychiatry'),
    'Pandemic': IllnessDetails(diagnostic=['General Diagnosis', 'X-Ray'], treatment='Pans Lab'),
    'Parapox': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Pipe Organs': IllnessDetails(diagnostic=['X-Ray', 'M.E.G.A Scan'], treatment='Surgery'),
    TPH_NAME_DISEASE_PT: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    'Portishead': IllnessDetails(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Ward'),
    'Potty Mouth': IllnessDetails(diagnostic=['Ward', 'Fluid Analysis'], treatment='Pharmacy'),
    'Predestinitis': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    TPH_NAME_DISEASE_PM: IllnessDetails(diagnostic=['Psychiatry', 'X-Ray'],
                                        treatment=TPH_NAME_ROOM_CR),
    'Pudding Blood': IllnessDetails(diagnostic=['Psychiatry', 'X-Ray'],
                                    treatment='Injection Room'),
    'Reptile Dysfunction': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Rock Bottom': IllnessDetails(diagnostic=['Fluid Analysis', 'DNA Lab'],
                                  treatment='Injection Room'),
    'Rock Star': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Rolling Stones': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Surgery'),
    'Shattered': IllnessDetails(diagnostic=['Ward', 'X-Ray'], treatment='Fracture Ward'),
    'Shock Horror': IllnessDetails(diagnostic=['Ward', 'Fluid Analysis'],
                                   treatment='Shock Clinic'),
    'Slackbladder': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    'Spinal Bap': IllnessDetails(diagnostic=['Cardiology', 'Fluid Analysis'], treatment='Surgery'),
    'Spontaneous Combustion': IllnessDetails(diagnostic=['M.E.G.A Scan', 'DNA Lab'],
                                             treatment='Injection Room'),
    'Tarred Pits': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Time Warts': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP], treatment='DNA Lab'),
    'Touch of Midas': IllnessDetails(diagnostic=['DNA Lab', 'M.E.G.A Scan'], treatment='DNA Lab'),
    'Turtle Head': IllnessDetails(diagnostic=['Fluid Analysis', 'X-Ray'], treatment='Head Office'),
    TPH_NAME_DISEASE_VD: IllnessDetails(diagnostic=['General Diagnosis'], treatment='Pharmacy'),
    'Woolly Man-Mouth': IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'Ward'], treatment='DNA Lab'),
}

TPH_ILLNESS_LIST = list(TPH_ILLNESS_DICT.keys())

# 3. MENUS

HOSPITAL_MENU = Menu('TWO POINT HOSPITALS', {i+1: TPH_HOSPITAL_LIST[i] for i in
                                             range(0, len(TPH_HOSPITAL_LIST))})
