"""Defines constants for the Two Point Science package.

Defines types and values used by the entire package.

    Typical usage example:

    from tps.tph_constants import (TPH_ROOM_DICT, TPH_ROOM_LIST)
"""

# Standard
from collections import namedtuple

# Third Party

# Local


# 1. DATA TYPES
HospitalDetails = namedtuple('HospitalDetails', 'illness')
IllnessDetails = namedtuple('IllnessDetails', 'diagnostic treatment')
# IllnessDetails = namedtuple('IllnessDetails', 'diagnostic treatment difficulty death health')
RoomDetails = namedtuple('RoomDetails', 'purpose')

# 2. MACROS

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
TPH_NAME_DISEASE_HIL = 'Historical Laughter'
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
                             'Night Fever', 'Potty Mouth', TPH_NAME_DISEASE_PM, 'Pudding Blood',
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
    TPH_NAME_DISEASE_HOL: IllnessDetails(diagnostic=[TPH_NAME_ROOM_GP, 'X-Ray'],
                                         treatment='Pharmacy'),
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
