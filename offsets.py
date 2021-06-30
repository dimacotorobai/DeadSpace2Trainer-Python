class DeadSpace:
    #Window Name
    windowName: str = 'Dead Space'

    #Credit and Nodes Offsets(Module Base + Offsets)
    node_offsets: tuple   = (0x00B4578C, 0x8, 0x38, 0xD0, 0x594)
    credit_offsets: tuple = (0x00B4578C, 0x8, 0x38, 0x18, 0x370, 0x5C)
    health_offsets: tuple = (0x00B4578C, 0x278, 0x38, 0x3E0)


    #Godmode
    godmode_offset: int = 0x5D1DD
    gotmode_size: int   = 8
    godmode_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90)
    godmode_off: tuple  = (0xF3, 0x0F, 0x11, 0x87, 0x20, 0x01, 0x00, 0x00)

    #Ammo
    ammo_offset: int = 0xF872E
    ammo_size: int   = 6
    ammo_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90, 0x90)
    ammo_off: tuple  = (0x89, 0xBE, 0x84, 0x06, 0x00, 0x00)

    #Air
    air_offset: int = 0x13481A
    air_size: int   = 5
    air_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90)
    air_off: tuple  = (0xF3, 0x0F, 0x11, 0x46, 0x70)

    #Stasis
    stasis_offset: int = 0x12735F
    stasis_size: int   = 8
    stasis_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90)
    stasis_off: tuple  = (0xF3, 0x0F, 0x11, 0x86, 0x28, 0x01, 0x00, 0x00)


class DeadSpace2:
    #Window Name
    windowName: str = 'Dead Space™ 2'

    #Credits and Nodes
    node_offsets:   tuple = (0x01CAB040, 0x58, 0x42C)
    credit_offsets: tuple = (0x01CA4610, 0x270, 0xBF8)
    health_offsets: tuple = (0x01C4D554, 0x18, 0x2C, 0xC, 0xE8)

    #Godmode
    godmode_offset: int = 0xB84D5C
    godmode_size: int   = 8
    godmode_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90)
    godmode_off: tuple  = (0xF3, 0x0F, 0x11, 0x87, 0xE8, 0x00, 0x00, 0x00)

    #Ammo
    ammo_offset: int = 0x9BAF57
    ammo_size: int   = 6
    ammo_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90, 0x90)
    ammo_off: tuple  = (0x89, 0xAE, 0x9C, 0x03, 0x00, 0x00)

    #Stasis
    stasis_offset: int = 0xB55D96
    stasis_size: int   = 8
    stasis_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90)
    stasis_off: tuple  = (0xF3, 0x0F, 0x11, 0x81, 0xF0, 0x00, 0x00, 0x00)

    #Air
    air_offset: int = 0x496916
    air_size: int   = 5
    air_on: tuple   = (0x90, 0x90, 0x90, 0x90, 0x90)
    air_off: tuple  = (0xF3, 0x0F, 0x11, 0x46, 0x74)

    