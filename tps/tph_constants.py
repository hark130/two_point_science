# Standard
from collections import namedtuple
# Third Party
# Local

# Data Types
Hospital_Details = namedtuple('Hospital_Details', 'illness')
Illness_Details = namedtuple('Illness_Details', 'diagnostic treatment')
Room_Details = namedtuple('Room_Details', 'purpose')

# MACROS
TPH_NAME_ROOM_GP = "GP's Office"
TPH_NAME_DISEASE_VERBAL = 'Verbal Diarrhoea'

TPH_ROOM_DICT = {
    'Cardiology':Room_Details(purpose='Diagnostic'),
    'Chromatherapy':Room_Details(purpose='Treatment'),
    'Clown Clinic':Room_Details(purpose='Treatment'),
    'Cryptology':Room_Details(purpose='Treatment'),
    'De-Lux Clinic':Room_Details(purpose='Treatment'),
    'DNA Lab':Room_Details(purpose='Both'),
    'Fluid Analysis':Room_Details(purpose='Diagnostic'),
    'Fracture Ward':Room_Details(purpose='Treatment'),
    'General Diagnosis':Room_Details(purpose='Diagnostic'),
    TPH_NAME_ROOM_GP:Room_Details(purpose='Diagnostic'),
    'Head Office':Room_Details(purpose='Treatment'),
    'Injection Room':Room_Details(purpose='Treatment'),
    'M.E.G.A Scan':Room_Details(purpose='Diagnostic'),
    'Pans Lab':Room_Details(purpose='Treatment'),
    'Pest Control':Room_Details(purpose='Treatment'),
    'Pharmacy':Room_Details(purpose='Treatment'),
    'Psychiatry':Room_Details(purpose='Both'),
    'Recurvery Room':Room_Details(purpose='Treatment'),
    'Resolution Lab':Room_Details(purpose='Treatment'),
    'Shock Clinic':Room_Details(purpose='Treatment'),
    'Surgery':Room_Details(purpose='Treatment'),
    'Ward':Room_Details(purpose='Both'),
    'X-Ray':Room_Details(purpose='Diagnostic'),
}

TPH_ROOM_LIST = TPH_ROOM_DICT.keys()

TPH_DIAGNOSTIC_LIST = [room for room, value in TPH_ROOM_DICT.items() if value.purpose in ['Diagnostic', 'Both']]

TPH_TREATMENT_LIST = [room for room, value in TPH_ROOM_DICT.items() if value.purpose in ['Treatment', 'Both']]

TPH_HOSPITAL_DICT = {
    'Blighton':Hospital_Details(illness=[]),
    'Camouflage Falls':Hospital_Details(illness=[]),
    'Chasm 24':Hospital_Details(illness=[]),
    'Clockwise-above-Thyme':Hospital_Details(illness=[]),
    'Clockwise-before-Thyme':Hospital_Details(illness=[]),
    'Clockwise-upon-Thyme':Hospital_Details(illness=[]),
    'Croquembouche':Hospital_Details(illness=[]),
    'Duckworth-upon-Bilge':Hospital_Details(illness=[]),
    'Fitzpocket Academy':Hospital_Details(illness=[]),
    'Flemington':Hospital_Details(illness=[]),
    'Flottering':Hospital_Details(illness=[]),
    'Goldpan':Hospital_Details(illness=[]),
    'Grockle Bay':Hospital_Details(illness=[TPH_NAME_DISEASE_VERBAL, 'Lazy Bones', 'Misery Guts',
        'Mucky Feet', 'Mime Crisis', 'Cubism', 'Inflated Ego', 'Jazz Hand', 'Rock Bottom',
        'Hurty Leg', 'Broken Face', '8-bitten', 'Floppy Discs', 'Emperor Complex', 'Denim Genes',
        'Turtle Head', 'Shock Horror', 'Pudding Blood', 'Leopard Skin', 'Heart Throb', 'Shattered',
        'Spontaneous Combustion', 'Jumbo DNA', 'Gurning Loins', 'Touch of Midas']),
    'Hostport':Hospital_Details(illness=[]),
    'Lower Bullocks':Hospital_Details(illness=[]),
    'Melt Downs':Hospital_Details(illness=[]),
    'Mitton University':Hospital_Details(illness=[]),
    'Mudbury Festival':Hospital_Details(illness=[]),
    'Old Newpoint':Hospital_Details(illness=[]),
    'Overgrowth':Hospital_Details(illness=[]),
    'Pebberley Reef':Hospital_Details(illness=[]),
    'Pelican Wharf':Hospital_Details(illness=[]),
    'Plywood Studios':Hospital_Details(illness=[]),
    'Roquefort Castle':Hospital_Details(illness=[]),
    'Rotting Hill':Hospital_Details(illness=[]),
}

TPH_HOSPITAL_LIST = TPH_HOSPITAL_DICT.keys()

TPH_ILLNESS_DICT = {
    '8-bitten':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Resolution Lab'),
    'Animal Magnetism':Illness_Details(diagnostic=['Cardiology', 'M.E.G.A Scan'], treatment='Pest Control'),
    'Artificial Intelligence':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP, 'Ward'], treatment='Psychiatry'),
    'Bed Face':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Ward'),
    'Boggled Mind':Illness_Details(diagnostic=['Ward', 'X-Ray'], treatment='Psychiatry'),
    'Bogwarts':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Pharmacy'),
    'Bone Head':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Surgery'),
    'Broken Face':Illness_Details(diagnostic=['Cardiology', 'Fluid Analysis'], treatment='Fracture Ward'),
    'Clamp':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Clockjaw':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Fracture Ward'),
    'Cod Piece':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Cross Bones':Illness_Details(diagnostic=['Psychiatry', 'X-Ray'], treatment='Fracture Ward'),
    'Cubism':Illness_Details(diagnostic=['Fluid Analysis', 'X-Ray'], treatment='Recurvery Room'),
    'Decision Rash':Illness_Details(diagnostic=['Fluid Analysis', 'Cardiology'], treatment='Injection Room'),
    'Denim Genes':Illness_Details(diagnostic=['Fluid Analysis', 'M.E.G.A Scan'], treatment='DNA Lab'),
    'Dino Sores':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Injection Room'),
    'Emperor Complex':Illness_Details(diagnostic=['DNA Lab', 'Cardiology'], treatment='Psychiatry'),
    'Floppy Discs':Illness_Details(diagnostic=['X-Ray', 'M.E.G.A Scan'], treatment='Surgery'),
    'Flumps':Illness_Details(diagnostic=['Cardiology', 'M.E.G.A Scan'], treatment='DNA Lab'),
    'Fomo Sapiens':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Forefraught':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Fossil Eyes':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP, 'DNA Lab'], treatment='DNA Lab'),
    'Fractured Timeline':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Fracture Ward'),
    'Freudian Lips':Illness_Details(diagnostic=['Cardiology', 'Psychiatry'], treatment='Psychiatry'),
    'Grey Anatomy':Illness_Details(diagnostic=['Fluid Analysis', 'M.E.G.A Scan'], treatment='Chromatherapy'),
    'Grout':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Gurning Loins':Illness_Details(diagnostic=['General Diagnosis', 'M.E.G.A Scan'], treatment='Surgery'),
    'Headcrabedness':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='De-Lux Clinic'),
    'Heart Throb':Illness_Details(diagnostic=['Cardiology', 'Fluid Analysis'], treatment='Surgery'),
    'Hotheadedness':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='De-Lux Clinic'),
    'Humerus Injury':Illness_Details(diagnostic=['General Diagnosis', 'Ward'], treatment='Fracture Ward'),
    'Hurty Leg':Illness_Details(diagnostic=['General Diagnosis', 'X-Ray'], treatment='Fracture Ward'),
    'Inflated Ego':Illness_Details(diagnostic=['Fluid Analysis', 'General Diagnosis'], treatment='Psychiatry'),
    'Jazz Hand':Illness_Details(diagnostic=['X-Ray', 'M.E.G.A Scan'], treatment='Ward'),
    'Jest Infection':Illness_Details(diagnostic=['Psychiatry', 'X-Ray'], treatment='Clown Clinic'),
    'Jumbo DNA':Illness_Details(diagnostic=['M.E.G.A Scan', 'Fluid Analysis'], treatment='DNA Lab'),
    'Lazy Bones':Illness_Details(diagnostic=['Cardiology', 'General Diagnosis'], treatment='Ward'),
    'Leopard Skin':Illness_Details(diagnostic=['Fluid Analysis', 'X-Ray'], treatment='DNA Lab'),
    'Lightheadedness':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='De-Lux Clinic'),
    'Lightheadedness (Frightheadedness)':Illness_Details(diagnostic=['', ''], treatment='De-Lux Clinic'),
    'Litter Bug':Illness_Details(diagnostic=['Fluid Analysis', 'X-Ray'], treatment='Injection Room'),
    'Loopy':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    'Lycanthropy':Illness_Details(diagnostic=['Cardiology', 'Fluid Analysis'], treatment='Pharmacy'),
    'Mime Crisis':Illness_Details(diagnostic=['Cardiology', 'Psychiatry'], treatment='Psychiatry'),
    'Misery Guts':Illness_Details(diagnostic=['Cardiology', 'Fluid Analysis'], treatment='Pharmacy'),
    'Missing Link':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP, 'M.E.G.A Scan'], treatment='Fracture Ward'),
    'Mock Star':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Psychiatry'),
    'Monobrow':Illness_Details(diagnostic=['Ward', 'X-Ray'], treatment='Ward'),
    'Mood Poisoning':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Injection Room'),
    'Mucky Feet':Illness_Details(diagnostic=['DNA Lab', 'X-Ray'], treatment='Ward'),
    'Night Fever':Illness_Details(diagnostic=['General Diagnosis', 'Psychiatry'], treatment='Psychiatry'),
    'Pandemic':Illness_Details(diagnostic=['General Diagnosis', 'X-Ray'], treatment='Pans Lab'),
    'Parapox':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Pipe Organs':Illness_Details(diagnostic=['X-Ray', 'M.E.G.A Scan'], treatment='Surgery'),
    'Portishead':Illness_Details(diagnostic=['General Diagnosis', 'Cardiology'], treatment='Ward'),
    'Potty Mouth':Illness_Details(diagnostic=['Ward', 'Fluid Analysis'], treatment='Pharmacy'),
    'Predestinitis':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    'Premature Mummification':Illness_Details(diagnostic=['Psychiatry', 'X-Ray'], treatment='Decrypter'),
    'Pudding Blood':Illness_Details(diagnostic=['Psychiatry', 'X-Ray'], treatment='Injection Room'),
    'Reptile Dysfunction':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Rock Bottom':Illness_Details(diagnostic=['Fluid Analysis', 'DNA Lab'], treatment='Injection Room'),
    'Rock Star':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Psychiatry'),
    'Rolling Stones':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Surgery'),
    'Shattered':Illness_Details(diagnostic=['Ward', 'X-Ray'], treatment='Fracture Ward'),
    'Shock Horror':Illness_Details(diagnostic=['Ward', 'Fluid Analysis'], treatment='Shock Clinic'),
    'Slackbladder':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Ward'),
    'Spinal Bap':Illness_Details(diagnostic=['Cardiology', 'Fluid Analysis'], treatment='Surgery'),
    'Spontaneous Combustion':Illness_Details(diagnostic=['M.E.G.A Scan', 'DNA Lab'], treatment='Injection Room'),
    'Tarred Pits':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='Pharmacy'),
    'Time Warts':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP], treatment='DNA Lab'),
    'Touch of Midas':Illness_Details(diagnostic=['DNA Lab', 'M.E.G.A Scan'], treatment='DNA Lab'),
    'Turtle Head':Illness_Details(diagnostic=['Fluid Analysis', 'X-Ray'], treatment='Head Office'),
    TPH_NAME_DISEASE_VERBAL:Illness_Details(diagnostic=['General Diagnosis'], treatment='Pharmacy'),
    'Woolly Man-Mouth':Illness_Details(diagnostic=[TPH_NAME_ROOM_GP, 'Ward'], treatment='DNA Lab'),
}

TPH_ILLNESS_LIST = TPH_ILLNESS_DICT.keys()
