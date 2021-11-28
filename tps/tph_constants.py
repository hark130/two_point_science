"""Defines constants for the Two Point Science package.

Defines types and values used by the entire package.

    Typical usage example:

    from tps.tph_constants import (MISSING_DATA, TPH_ILLNESS_DICT, TPH_NAME_DISEASE_8B)

    eight_bit = TPH_ILLNESS_DICT[TPH_NAME_DISEASE_8B]
    if eight_bit.health == MISSING_DATA:
        print('We still need to extricate this data point from Two Point Hospital')
    else:
        print(f"{TPH_NAME_DISEASE_8B}'s health constant is {eight_bit.health}"')
"""

# Standard
from collections import namedtuple

# Third Party

# Local
from tps.missing_data import MissingData


# 1. DATA TYPES
HospitalDetails = namedtuple('HospitalDetails', 'illness')
IllnessDetails = namedtuple('IllnessDetails', 'diagnostic treatment difficulty death decline')
RoomDetails = namedtuple('RoomDetails', 'purpose')

# 2. MACROS
# This macro indicates some game data is missing
MISSING_DATA = MissingData("TO DO: DON'T DO NOW... Get this data")

# DISEASE NAMES
# NOTE: Disease macro names were truncated to represent the acronym (for names with more than
#   one word) or just enough letters of the name to be unique (min: 2).
TPH_NAME_DISEASE_8B = '8-bitten'
TPH_NAME_DISEASE_AM = 'Animal Magnetism'
TPH_NAME_DISEASE_AI = 'Artificial Intelligence'
TPH_NAME_DISEASE_BEF = 'Bed Face'
TPH_NAME_DISEASE_BE = 'Beheadedness'
TPH_NAME_DISEASE_BP = 'Bionic Plague'
TPH_NAME_DISEASE_BOA = 'Bloat of Arms'
TPH_NAME_DISEASE_BM = 'Boggled Mind'
TPH_NAME_DISEASE_BO = 'Bogwarts'
TPH_NAME_DISEASE_BH = 'Bone Head'
TPH_NAME_DISEASE_BRF = 'Broken Face'
TPH_NAME_DISEASE_BY = 'Byteheadedness'
TPH_NAME_DISEASE_CAR = 'Chewed a Rose'
TPH_NAME_DISEASE_CLA = 'Clamp'
TPH_NAME_DISEASE_CLO = 'Clockjaw'
TPH_NAME_DISEASE_CP = 'Cod Piece'
TPH_NAME_DISEASE_CB = 'Cross Bones'
TPH_NAME_DISEASE_CU = 'Cubism'
TPH_NAME_DISEASE_DR = 'Decision Rash'
TPH_NAME_DISEASE_DG = 'Denim Genes'
TPH_NAME_DISEASE_DS = 'Dino Sores'
TPH_NAME_DISEASE_EC = 'Emperor Complex'
TPH_NAME_DISEASE_FD = 'Floppy Discs'
TPH_NAME_DISEASE_FLU = 'Flumps'
TPH_NAME_DISEASE_FS = 'Fomo Sapiens'
TPH_NAME_DISEASE_FO = 'Forefraught'
TPH_NAME_DISEASE_FE = 'Fossil Eyes'
TPH_NAME_DISEASE_FT = 'Fractured Timeline'
TPH_NAME_DISEASE_FL = 'Freudian Lips'
TPH_NAME_DISEASE_FU = 'Futurism'
TPH_NAME_DISEASE_GA = 'Grey Anatomy'
TPH_NAME_DISEASE_GD = 'Glass Dome'
TPH_NAME_DISEASE_GR = 'Grout'
TPH_NAME_DISEASE_GL = 'Gurning Loins'
TPH_NAME_DISEASE_HC = 'Hacking Cough'
TPH_NAME_DISEASE_HE = 'Headcrabedness'
TPH_NAME_DISEASE_HT = 'Heart Throb'
TPH_NAME_DISEASE_HL = 'Historical Laughter'
TPH_NAME_DISEASE_HOL = 'Hologlands'
TPH_NAME_DISEASE_HOT = 'Hotheadedness'
TPH_NAME_DISEASE_HI = 'Humerus Injury'
TPH_NAME_DISEASE_HUL = 'Hurty Leg'
TPH_NAME_DISEASE_IE = 'Inflated Ego'
TPH_NAME_DISEASE_JH = 'Jazz Hand'
TPH_NAME_DISEASE_JI = 'Jest Infection'
TPH_NAME_DISEASE_JRI = 'Jester Infection'
TPH_NAME_DISEASE_JD = 'Jumbo DNA'
TPH_NAME_DISEASE_LAB = 'Lazy Bones'
TPH_NAME_DISEASE_LS = 'Leopard Skin'
TPH_NAME_DISEASE_LI = 'Lightheadedness'
TPH_NAME_DISEASE_FR = 'Lightheadedness (Frightheadedness)'
TPH_NAME_DISEASE_LIB = 'Litter Bug'
TPH_NAME_DISEASE_LO = 'Loopy'
TPH_NAME_DISEASE_LY = 'Lycanthropy'
TPH_NAME_DISEASE_MC = 'Mime Crisis'
TPH_NAME_DISEASE_MG = 'Misery Guts'
TPH_NAME_DISEASE_ML = 'Missing Link'
TPH_NAME_DISEASE_MS = 'Mock Star'
TPH_NAME_DISEASE_MO = 'Monobrow'
TPH_NAME_DISEASE_MP = 'Mood Poisoning'
TPH_NAME_DISEASE_MF = 'Mucky Feet'
TPH_NAME_DISEASE_NF = 'Night Fever'
TPH_NAME_DISEASE_PAN = 'Pandemic'
TPH_NAME_DISEASE_PAR = 'Parapox'
TPH_NAME_DISEASE_PO = 'Pipe Organs'
TPH_NAME_DISEASE_PT = 'Pneumatic Tubes'
TPH_NAME_DISEASE_POR = 'Portishead'
TPH_NAME_DISEASE_PM = 'Potty Mouth'
TPH_NAME_DISEASE_PR = 'Predestinitis'
TPH_NAME_DISEASE_PRM = 'Premature Mummification'
TPH_NAME_DISEASE_PB = 'Pudding Blood'
TPH_NAME_DISEASE_RD = 'Reptile Dysfunction'
TPH_NAME_DISEASE_RB = 'Rock Bottom'
TPH_NAME_DISEASE_RKS = 'Rock Star'
TPH_NAME_DISEASE_RGS = 'Rolling Stones'
TPH_NAME_DISEASE_SHA = 'Shattered'
TPH_NAME_DISEASE_SH = 'Shock Horror'
TPH_NAME_DISEASE_SL = 'Slackbladder'
TPH_NAME_DISEASE_SB = 'Spinal Bap'
TPH_NAME_DISEASE_SC = 'Spontaneous Combustion'
TPH_NAME_DISEASE_TP = 'Tarred Pits'
TPH_NAME_DISEASE_TW = 'Time Warts'
TPH_NAME_DISEASE_TOM = 'Touch of Midas'
TPH_NAME_DISEASE_TH = 'Turtle Head'
TPH_NAME_DISEASE_VD = 'Verbal Diarrhoea'
TPH_NAME_DISEASE_WMM = 'Woolly Man-Mouth'


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
TPH_NAME_ROOM_CA = 'Cardiology'
TPH_NAME_ROOM_CH = 'Chromatherapy'
TPH_NAME_ROOM_CL = 'Clown Clinic'
TPH_NAME_ROOM_CR = 'Cryptology'
TPH_NAME_ROOM_DLC = 'De-Lux Clinic'
TPH_NAME_ROOM_DL = 'DNA Lab'
TPH_NAME_ROOM_FA = 'Fluid Analysis'
TPH_NAME_ROOM_FW = 'Fracture Ward'
TPH_NAME_ROOM_GD = 'General Diagnosis'
TPH_NAME_ROOM_GP = "GP's Office"
TPH_NAME_ROOM_HO = 'Head Office'
TPH_NAME_ROOM_IR = 'Injection Room'
TPH_NAME_ROOM_MS = 'M.E.G.A Scan'
TPH_NAME_ROOM_PL = 'Pans Lab'
TPH_NAME_ROOM_PC = 'Pest Control'
TPH_NAME_ROOM_PH = 'Pharmacy'
TPH_NAME_ROOM_PSY = 'Psychiatry'
TPH_NAME_ROOM_RR = 'Recurvery Room'
TPH_NAME_ROOM_RL = 'Resolution Lab'
TPH_NAME_ROOM_SC = 'Shock Clinic'
TPH_NAME_ROOM_SU = 'Surgery'
TPH_NAME_ROOM_WA = 'Ward'
TPH_NAME_ROOM_XR = 'X-Ray'


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
    # Blighton
    # https://two-point-hospital.fandom.com/wiki/Blighton
    TPH_NAME_HOSPITAL_BL:
    HospitalDetails(illness=['8-bitten', 'Animal Magnetism', 'Cubism', 'Decision Rash',
                             'Emperor Complex', 'Freudian Lips', 'Grey Anatomy', 'Gurning Loins',
                             'Heart Throb', 'Leopard Skin', 'Litter Bug', 'Lycanthropy',
                             'Mime Crisis', 'Misery Guts', 'Mock Star', 'Mood Poisoning',
                             'Night Fever', TPH_NAME_DISEASE_PM, 'Pudding Blood',
                             'Rock Bottom', 'Shock Horror', 'Spinal Bap', 'Spontaneous Combustion',
                             'Touch of Midas', 'Turtle Head', TPH_NAME_DISEASE_VD]),
    'Camouflage Falls': HospitalDetails(illness=[]),
    'Chasm 24': HospitalDetails(illness=[]),
    # Clockwise-above-Thyme
    TPH_NAME_HOSPITAL_CAT:
    HospitalDetails(illness=['Jest Infection', TPH_NAME_DISEASE_JRI, TPH_NAME_DISEASE_BE,
                             TPH_NAME_DISEASE_BY, TPH_NAME_DISEASE_HOT, 'Lightheadedness',
                             'Fossil Eyes', 'Jumbo DNA', 'Time Warts', 'Woolly Man-Mouth',
                             'Clockjaw', 'Fractured Timeline', TPH_NAME_DISEASE_GD, 'Missing Link',
                             TPH_NAME_DISEASE_BOA, 'Dino Sores', TPH_NAME_DISEASE_HC,
                             'Pudding Blood', TPH_NAME_DISEASE_CAR, 'Cod Piece',
                             TPH_NAME_DISEASE_HOL, 'Misery Guts', 'Parapox',
                             'Artificial Intelligence', 'Fomo Sapiens', TPH_NAME_DISEASE_HL,
                             'Reptile Dysfunction', 'Cubism', TPH_NAME_DISEASE_FU,
                             TPH_NAME_DISEASE_BP, 'Bone Head', 'Rolling Stones', 'Loopy',
                             'Monobrow', TPH_NAME_DISEASE_PT, 'Predestinitis']),
    'Clockwise-before-Thyme': HospitalDetails(illness=[]),
    'Clockwise-upon-Thyme': HospitalDetails(illness=[]),
    # Croquembouche
    # https://two-point-hospital.fandom.com/wiki/Croquembouche
    TPH_NAME_HOSPITAL_CR:
    HospitalDetails(illness=['Grey Anatomy', 'Jest Infection', 'Premature Mummification',
                             'Headcrabedness', 'Lightheadedness', 'Denim Genes', 'Flumps',
                             'Jumbo DNA', 'Leopard Skin', 'Touch of Midas', 'Broken Face',
                             'Cross Bones', 'Humerus Injury', 'Hurty Leg', 'Shattered',
                             'Turtle Head', 'Decision Rash', 'Litter Bug', 'Mood Poisoning',
                             'Pudding Blood', 'Rock Bottom', 'Spontaneous Combustion', 'Pandemic',
                             'Animal Magnetism', 'Bogwarts', 'Lycanthropy', 'Misery Guts',
                             'Potty Mouth', 'Verbal Diarrhoea', 'Boggled Mind', 'Emperor Complex',
                             'Freudian Lips', 'Inflated Ego', 'Mime Crisis', 'Mock Star',
                             'Night Fever', 'Cubism', '8-bitten', 'Shock Horror', 'Floppy Discs',
                             'Gurning Loins', 'Heart Throb', 'Pipe Organs', 'Spinal Bap',
                             'Bed Face', 'Jazz Hand', 'Lazy Bones', 'Monobrow', 'Mucky Feet',
                             'Portishead']),
    'Duckworth-upon-Bilge': HospitalDetails(illness=[]),
    'Fitzpocket Academy': HospitalDetails(illness=[]),
    'Flemington': HospitalDetails(illness=[]),
    'Flottering': HospitalDetails(illness=[]),
    'Goldpan': HospitalDetails(illness=[]),
    # Grockle Bay
    # https://two-point-hospital.fandom.com/wiki/Grockle_Bay
    # TPH_NAME_HOSPITAL_GB:
    # HospitalDetails(illness=['Denim Genes', 'Leopard Skin', 'Touch of Midas', 'Broken Face',
    #                          'Hurty Leg', 'Shattered', 'Turtle Head', 'Pudding Blood',
    #                          'Rock Bottom', 'Spontaneous Combustion', 'Misery Guts',
    #                          TPH_NAME_DISEASE_VD, 'Emperor Complex', 'Inflated Ego',
    #                          'Mime Crisis',
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
    # Mitton University
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
    # Pelican Wharf
    # https://two-point-hospital.fandom.com/wiki/Pelican_Wharf
    TPH_NAME_HOSPITAL_PW:
    HospitalDetails(illness=['Grey Anatomy', 'Jest Infection', 'Premature Mummification',
                             'Headcrabedness', 'Lightheadedness', 'Jumbo DNA', 'Leopard Skin',
                             'Touch of Midas', 'Broken Face', 'Cross Bones', 'Shattered',
                             'Turtle Head', 'Decision Rash', 'Litter Bug', 'Pudding Blood',
                             'Rock Bottom', 'Spontaneous Combustion', 'Pandemic',
                             'Animal Magnetism', 'Bogwarts', 'Lycanthropy', 'Misery Guts',
                             'Potty Mouth', 'Boggled Mind', 'Emperor Complex', 'Inflated Ego',
                             'Mock Star', 'Night Fever', 'Cubism', '8-bitten', 'Shock Horror',
                             'Gurning Loins', 'Heart Throb', 'Pipe Organs', 'Jazz Hand',
                             'Monobrow', 'Mucky Feet', 'Portishead']),
    'Plywood Studios': HospitalDetails(illness=[]),
    'Roquefort Castle': HospitalDetails(illness=[]),
    # Rotting Hill
    # https://two-point-hospital.fandom.com/wiki/Rotting_Hill
    TPH_NAME_HOSPITAL_RH:
    HospitalDetails(illness=['Grey Anatomy', 'Jest Infection', 'Premature Mummification',
                             'Headcrabedness', 'Lightheadedness', 'Flumps', 'Jumbo DNA',
                             'Humerus Injury', 'Hurty Leg', 'Shattered', 'Turtle Head',
                             'Litter Bug', 'Mood Poisoning', 'Spontaneous Combustion', 'Pandemic',
                             'Potty Mouth', 'Verbal Diarrhoea', 'Emperor Complex', 'Mock Star',
                             'Night Fever', 'Cubism', 'Floppy Discs', 'Gurning Loins',
                             'Pipe Organs', 'Bed Face', 'Lazy Bones', 'Monobrow', 'Mucky Feet',
                             'Portishead']),
    # Smogley
    TPH_NAME_HOSPITAL_SM:
    HospitalDetails(illness=['Grey Anatomy', 'Cross Bones', 'Humerus Injury', 'Hurty Leg',
                             'Turtle Head', 'Decision Rash', 'Mood Poisoning',
                             'Spontaneous Combustion', 'Pandemic', 'Animal Magnetism',
                             'Floppy Discs', 'Gurning Loins', 'Heart Throb', 'Pipe Organs',
                             'Spinal Bap', 'Bed Face', 'Jazz Hand', 'Portishead']),
    # Sweaty Palms
    # https://two-point-hospital.fandom.com/wiki/Sweaty_Palms
    TPH_NAME_HOSPITAL_SP:
    HospitalDetails(illness=['Grey Anatomy', 'Jest Infection', 'Premature Mummification',
                             'Headcrabedness', 'Lightheadedness', 'Denim Genes', 'Flumps',
                             'Jumbo DNA', 'Touch of Midas', 'Broken Face', 'Cross Bones',
                             'Humerus Injury', 'Turtle Head', 'Decision Rash', 'Litter Bug',
                             'Spontaneous Combustion', 'Animal Magnetism', 'Pandemic', 'Bogwarts',
                             'Clamp', 'Lycanthropy', 'Verbal Diarrhoea', 'Boggled Mind',
                             'Emperor Complex', 'Freudian Lips', 'Night Fever', 'Cubism',
                             '8-bitten', 'Shock Horror', 'Gurning Loins', 'Pipe Organs',
                             'Lazy Bones', 'Jazz Hand', 'Portishead']),
    'Swelbard': HospitalDetails(illness=[]),
    'Topless Mountain': HospitalDetails(illness=[]),
    'Tumble': HospitalDetails(illness=[]),
    'Underlook Hotel': HospitalDetails(illness=[]),
    'Wanderoff': HospitalDetails(illness=[]),
    'Windsock': HospitalDetails(illness=[]),
}

TPH_HOSPITAL_LIST = list(TPH_HOSPITAL_DICT.keys())

TPH_ILLNESS_DICT = {
    TPH_NAME_DISEASE_8B: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_RL, difficulty=0.5, death=.5, decline=1),
    TPH_NAME_DISEASE_AM: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_PC, difficulty=0.4, death=.25, decline=0.75),
    TPH_NAME_DISEASE_AI: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_WA], treatment=TPH_NAME_ROOM_PSY, difficulty=0.7, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_BEF: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_WA, difficulty=0.2, death=.1, decline=0.5),
    TPH_NAME_DISEASE_BE: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_DLC, difficulty=0.2, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_BP: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_SU, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_BOA: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_IR, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_BM: IllnessDetails(diagnostic=[TPH_NAME_ROOM_WA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_PSY, difficulty=0.6, death=0, decline=0.1),
    TPH_NAME_DISEASE_BO: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_PH, difficulty=0.4, death=.2, decline=1),
    TPH_NAME_DISEASE_BH: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_SU, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_BRF: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_FW, difficulty=0.5, death=.3, decline=1),
    TPH_NAME_DISEASE_BY: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_DLC, difficulty=0.2, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_CAR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PH, difficulty=0.5, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_CLA: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PH, difficulty=0.1, death=0, decline=0.75),
    TPH_NAME_DISEASE_CLO: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_FW, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_CP: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PH, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_CB: IllnessDetails(diagnostic=[TPH_NAME_ROOM_PSY, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_FW, difficulty=0.6, death=.3, decline=1),
    TPH_NAME_DISEASE_CU: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_RR, difficulty=0.5, death=1, decline=1),
    TPH_NAME_DISEASE_DR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_IR, difficulty=0.6, death=.4, decline=1),
    TPH_NAME_DISEASE_DG: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_DL, difficulty=0.4, death=1, decline=1),
    TPH_NAME_DISEASE_DS: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_IR, difficulty=0.5, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_EC: IllnessDetails(diagnostic=[TPH_NAME_ROOM_DL, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_PSY, difficulty=0.7, death=0, decline=0.1),
    TPH_NAME_DISEASE_FD: IllnessDetails(diagnostic=[TPH_NAME_ROOM_XR, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_SU, difficulty=0.4, death=.5, decline=1),
    TPH_NAME_DISEASE_FLU: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_DL, difficulty=0.5, death=1, decline=1),
    TPH_NAME_DISEASE_FS: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PSY, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_FO: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PSY, difficulty=0.3, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_FE: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_DL], treatment=TPH_NAME_ROOM_DL, difficulty=0.5, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_FT: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_FW, difficulty=0.5, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_FL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_PSY], treatment=TPH_NAME_ROOM_PSY, difficulty=0.3, death=0, decline=0.1),
    TPH_NAME_DISEASE_FU: IllnessDetails(diagnostic=[TPH_NAME_ROOM_DL, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_RR, difficulty=0.5, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_GD: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_WA], treatment=TPH_NAME_ROOM_FW, difficulty=0.8, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_GA: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_CH, difficulty=0.4, death=0, decline=0.75),
    TPH_NAME_DISEASE_GR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PH, difficulty=0, death=0, decline=0.5),
    TPH_NAME_DISEASE_GL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_SU, difficulty=0.8, death=.5, decline=1),
    TPH_NAME_DISEASE_HC: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_IR, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_HE: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_DLC, difficulty=0.2, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_HT: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_SU, difficulty=0.6, death=.5, decline=1),
    TPH_NAME_DISEASE_HL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PSY, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_HOL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_PH, difficulty=0.7, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_HOT: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_DLC, difficulty=0.2, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_HI: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_WA], treatment=TPH_NAME_ROOM_FW, difficulty=0.2, death=.3, decline=1),
    TPH_NAME_DISEASE_HUL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_FW, difficulty=0.3, death=.3, decline=1),
    TPH_NAME_DISEASE_IE: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_GD], treatment=TPH_NAME_ROOM_PSY, difficulty=0.5, death=0, decline=0.1),
    TPH_NAME_DISEASE_JH: IllnessDetails(diagnostic=[TPH_NAME_ROOM_XR, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_WA, difficulty=0.7, death=.1, decline=1),
    TPH_NAME_DISEASE_JI: IllnessDetails(diagnostic=[TPH_NAME_ROOM_PSY, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_CL, difficulty=0.4, death=0, decline=0.1),
    TPH_NAME_DISEASE_JRI: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_CL, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_JD: IllnessDetails(diagnostic=[TPH_NAME_ROOM_MS, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_DL, difficulty=0.7, death=1, decline=1),
    TPH_NAME_DISEASE_LAB: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_GD], treatment=TPH_NAME_ROOM_WA, difficulty=0.5, death=.1, decline=0.75),
    TPH_NAME_DISEASE_LS: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_DL, difficulty=0.6, death=1, decline=1),
    TPH_NAME_DISEASE_LI: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_DLC, difficulty=0.2, death=1, decline=0.75),
    TPH_NAME_DISEASE_FR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_DLC, difficulty=0.2, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_LIB: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_IR, difficulty=0.5, death=.4, decline=1),
    TPH_NAME_DISEASE_LO: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_WA, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_LY: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_PH, difficulty=0.7, death=.2, decline=1),
    TPH_NAME_DISEASE_MC: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_PSY], treatment=TPH_NAME_ROOM_PSY, difficulty=0.4, death=0, decline=0.1),
    TPH_NAME_DISEASE_MG: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_PH, difficulty=0.5, death=.2, decline=1),
    TPH_NAME_DISEASE_ML: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_FW, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_MS: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_PSY, difficulty=0.2, death=0, decline=0.1),
    TPH_NAME_DISEASE_MO: IllnessDetails(diagnostic=[TPH_NAME_ROOM_WA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_WA, difficulty=0.5, death=.1, decline=1),
    TPH_NAME_DISEASE_MP: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_IR, difficulty=0.3, death=.4, decline=1.5),
    TPH_NAME_DISEASE_MF: IllnessDetails(diagnostic=[TPH_NAME_ROOM_DL, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_WA, difficulty=0.6, death=.1, decline=1),
    TPH_NAME_DISEASE_NF: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_PSY], treatment=TPH_NAME_ROOM_PSY, difficulty=0.5, death=0, decline=0.1),
    TPH_NAME_DISEASE_PAN: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_PL, difficulty=0.3, death=.25, decline=0.75),
    TPH_NAME_DISEASE_PAR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PH, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_PO: IllnessDetails(diagnostic=[TPH_NAME_ROOM_XR, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_SU, difficulty=0.5, death=.5, decline=1),
    TPH_NAME_DISEASE_PT: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_WA, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_POR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, TPH_NAME_ROOM_CA], treatment=TPH_NAME_ROOM_WA, difficulty=0.4, death=.1, decline=1),
    TPH_NAME_DISEASE_PM: IllnessDetails(diagnostic=[TPH_NAME_ROOM_WA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_PH, difficulty=0.6, death=.2, decline=1),
    TPH_NAME_DISEASE_PR: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_WA, difficulty=0.7, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_PRM: IllnessDetails(diagnostic=[TPH_NAME_ROOM_PSY, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_CR, difficulty=0.5, death=.25, decline=1),
    TPH_NAME_DISEASE_PB: IllnessDetails(diagnostic=[TPH_NAME_ROOM_PSY, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_IR, difficulty=0.7, death=.4, decline=1),
    TPH_NAME_DISEASE_RD: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PSY, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_RB: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_DL], treatment=TPH_NAME_ROOM_IR, difficulty=0.4, death=.4, decline=1),
    TPH_NAME_DISEASE_RKS: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PSY, difficulty=0.2, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_RGS: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_SU, difficulty=0.3, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_SHA: IllnessDetails(diagnostic=[TPH_NAME_ROOM_WA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_FW, difficulty=0.8, death=.3, decline=1),
    TPH_NAME_DISEASE_SH: IllnessDetails(diagnostic=[TPH_NAME_ROOM_WA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_SC, difficulty=0.5, death=.5, decline=1),
    TPH_NAME_DISEASE_SL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_WA, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_SB: IllnessDetails(diagnostic=[TPH_NAME_ROOM_CA, TPH_NAME_ROOM_FA], treatment=TPH_NAME_ROOM_SU, difficulty=0.3, death=.5, decline=1),
    TPH_NAME_DISEASE_SC: IllnessDetails(diagnostic=[TPH_NAME_ROOM_MS, TPH_NAME_ROOM_DL], treatment=TPH_NAME_ROOM_IR, difficulty=0.8, death=.4, decline=1),
    TPH_NAME_DISEASE_TP: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_PH, difficulty=0.5, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_TW: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, ], treatment=TPH_NAME_ROOM_DL, difficulty=0.4, death=MISSING_DATA, decline=MISSING_DATA),
    TPH_NAME_DISEASE_TOM: IllnessDetails(diagnostic=[TPH_NAME_ROOM_DL, TPH_NAME_ROOM_MS], treatment=TPH_NAME_ROOM_DL, difficulty=0.8, death=1, decline=1),
    TPH_NAME_DISEASE_TH: IllnessDetails(diagnostic=[TPH_NAME_ROOM_FA, TPH_NAME_ROOM_XR], treatment=TPH_NAME_ROOM_HO, difficulty=0.5, death=.5, decline=1),
    TPH_NAME_DISEASE_VD: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GD, ], treatment=TPH_NAME_ROOM_PH, difficulty=0.2, death=.2, decline=0.75),
    TPH_NAME_DISEASE_WMM: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, TPH_NAME_ROOM_WA], treatment=TPH_NAME_ROOM_DL, difficulty=0.6, death=MISSING_DATA, decline=MISSING_DATA),
}

TPH_ILLNESS_LIST = list(TPH_ILLNESS_DICT.keys())
