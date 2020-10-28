from sys import argv

if len(argv) < 2:
    print('Usage: %s [bytes]' % __file__)
string = argv[1:]
# string = 'FE 07 20 06 06 EA 0E AA 18 17 FA 4D D8 CB 57 28 08 21 C5 D2 2A 47 4E 18 08 CD 41 2E 47 CD 41 2E 4F 21 0C D2 78 22 71 3E 46 EA 12 D2 FA 43 D1 EA 13 D2'.split()

bytestream = [int(x, 16) for x in string]

new = []

i = 0
while i < len(string):
    cmd = bytestream[i]
    if cmd == 0x00:   # nop
        print('nop')
        i += 1
    elif cmd == 0x01:  # ld bc,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('ld bc,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3
    elif cmd == 0x02:  # ld (bc),a
        print('ld (bc),a')
        i += 1
    elif cmd == 0x03:  # inc bc
        print('inc bc')
        i += 1
    elif cmd == 0x04:  # inc b
        print('inc b')
        i += 1
    elif cmd == 0x05:  # dec b
        print('dec b')
        i += 1
    elif cmd == 0x06:  # ld b,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld b, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2
    elif cmd == 0x07:  # rlca
        print('rlca')
        i += 1
    elif cmd == 0x08:  # ld ($aabb),sp
        nextbytes = bytestream[i+1:i+3]
        print('ld ($%s%s),sp' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3
    elif cmd == 0x09:  # add hl,bc
        print('add hl,bc')
        i += 1
    elif cmd == 0x0A:  # ld a,(bc)
        print('ld a,(bc)')
        i += 1
    elif cmd == 0x0B:  # dec bc
        i += 1
        print('dec bc')
    elif cmd == 0x0C:  # inc c
        i += 1
        print('inc c')
    elif cmd == 0x0D:  # dec c
        i += 1
        print('dec c')
    elif cmd == 0x0E:  # ld c,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld c, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2
    elif cmd == 0x0F:  # rrca
        print('rrca')
        i += 1
    elif cmd == 0x10:  # stop
        nextbytes = bytestream[i+1:i+2]
        print('stop')
        i += 2
    elif cmd == 0x11:  # ld de,$xxyy
        nextbytes = bytestream[i+1:i+3]
        print('ld de,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3
    elif cmd == 0x12:  # ld (de),a
        print('ld (de),a')
        i += 1
    elif cmd == 0x13:  # inc de
        print('inc de')
        i += 1
    elif cmd == 0x14:  # inc d
        print('inc d')
        i += 1
    elif cmd == 0x15:  # dec d
        print('dec d')
        i += 1
    elif cmd == 0x16:  # ld d,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld d, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2
    elif cmd == 0x17:  # rla
        print('rla')
        i += 1
    elif cmd == 0x18:  # jr $xx
        nextbytes = bytestream[i+1:i+2]
        print('jr $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2
    elif cmd == 0x19:  # add hl,de
        print('add hl,de')
        i += 1
    elif cmd == 0x1A:  # ld a,(de)
        print('ld a,(de)')
        i += 1
    elif cmd == 0x1B:  # dec de
        print('dec de')
        i += 1
    elif cmd == 0x1C:  # inc e
        print('inc e')
        i += 1
    elif cmd == 0x1D:  # dec e
        print('dec e')
        i += 1
    elif cmd == 0x1E:  # ld e,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld e, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2
    elif cmd == 0x1F:  # rra
        print('rra')
        i += 1
    elif cmd == 0x20:  # jr nz,$xx
        nextbytes = bytestream[i+1:i+2]
        print('jr nz, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2
    elif cmd == 0x21:  # ld hl,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('ld hl,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3
    elif cmd == 0x22:  # ld (hli),a
        print('ld (hli),a')
        i += 1
    elif cmd == 0x23:  # inc hl
        print('inc hl')
        i += 1
    elif cmd == 0x24:  # inc h
        print('inc h')
        i += 1
    elif cmd == 0x25:  # dec h
        print('dec h')
        i += 1
    elif cmd == 0x26:  # ld h,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld h, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x27:  # daa
        print('daa')
        i += 1

    elif cmd == 0x28:  # jr z,$xx
        nextbytes = bytestream[i+1:i+2]
        print('jr z, $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x29:  # add hl,hl
        print('add hl,hl')
        i += 1

    elif cmd == 0x2A:  # ld a,(hli)
        print('ld a,(hli)')
        i += 1

    elif cmd == 0x2B:  # dec hl
        print('dec hl')
        i += 1

    elif cmd == 0x2C:  # inc l
        print('inc l')
        i += 1

    elif cmd == 0x2D:  # dec l
        print('dec l')
        i += 1

    elif cmd == 0x2E:  # ld l,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld l,$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x2F:  # cpl
        print('cpl')
        i += 1

    elif cmd == 0x30:  # jr nc,$xx
        nextbytes = bytestream[i+1:i+2]
        print('jr nc,$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x31:  # ld sp,$xxyy
        nextbytes = bytestream[i+1:i+3]
        print('ld sp,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0x32:  # ldd (hl),a
        print('ldd (hl),a')
        i += 1

    elif cmd == 0x33:  # inc sp
        print('inc sp')
        i += 1

    elif cmd == 0x34:  # inc (hl)
        print('inc (hl)')
        i += 1

    elif cmd == 0x35:  # dec (hl)
        print('dec (hl)')
        i += 1

    elif cmd == 0x36:  # ld (hl),$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld (hl),$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x37:  # scf
        print('scf')
        i += 1

    elif cmd == 0x38:  # jr c,$xx
        nextbytes = bytestream[i+1:i+2]
        print('jr c,$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x39:  # add hl,sp
        print('add hl,sp')
        i += 1

    elif cmd == 0x3A:  # ldd a,(hl)
        print('ldd a,(hl)')
        i += 1

    elif cmd == 0x3B:  # dec sp
        print('dec sp')
        i += 1

    elif cmd == 0x3C:  # inc a
        print('inc a')
        i += 1

    elif cmd == 0x3D:  # dec a
        print('dec a')
        i += 1

    elif cmd == 0x3E:  # ld a,$xx
        nextbytes = bytestream[i+1:i+2]
        print('ld a,$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0x3F:  # ccf
        print('ccf')
        i += 1

    elif cmd == 0x40:  # ld b,b
        print('ld b,b')
        i += 1

    elif cmd == 0x41:  # ld b,c
        print('ld b,c')
        i += 1

    elif cmd == 0x42:  # ld b,d
        print('ld b,d')
        i += 1

    elif cmd == 0x43:  # ld b,e
        print('ld b,e')
        i += 1

    elif cmd == 0x44:  # ld b,h
        print('ld b,h')
        i += 1

    elif cmd == 0x45:  # ld b,l
        print('ld b,l')
        i += 1

    elif cmd == 0x46:  # ld b,(hl)
        print('ld b,(hl)')
        i += 1

    elif cmd == 0x47:  # ld b,a
        print('ld b,a')
        i += 1

    elif cmd == 0x48:  # ld c,b
        print('ld c,b')
        i += 1

    elif cmd == 0x49:  # ld c,c
        print('ld c,c')
        i += 1

    elif cmd == 0x4A:  # ld c,d
        print('ld c,d')
        i += 1

    elif cmd == 0x4B:  # ld c,e
        print('ld c,e')
        i += 1

    elif cmd == 0x4C:  # ld c,h
        print('ld c,h')
        i += 1

    elif cmd == 0x4D:  # ld c,l
        print('ld c,l')
        i += 1

    elif cmd == 0x4E:  # ld c,(hl)
        print('ld c,(hl)')
        i += 1

    elif cmd == 0x4F:  # ld c,a
        print('ld c,a')
        i += 1

    elif cmd == 0x50:  # ld d,b
        print('ld d,b')
        i += 1

    elif cmd == 0x51:  # ld d,c
        print('ld d,c')
        i += 1

    elif cmd == 0x52:  # ld d,d
        print('ld d,d')
        i += 1

    elif cmd == 0x53:  # ld d,e
        print('ld d,e')
        i += 1

    elif cmd == 0x54:  # ld d,h
        print('ld d,h')
        i += 1

    elif cmd == 0x55:  # ld d,l
        print('ld d,l')
        i += 1

    elif cmd == 0x56:  # ld d,(hl)
        print('ld d,(hl)')
        i += 1

    elif cmd == 0x57:  # ld d,a
        print('ld d,a')
        i += 1

    elif cmd == 0x58:  # ld e,b
        print('ld e,b')
        i += 1

    elif cmd == 0x59:  # ld e,c
        print('ld e,c')
        i += 1

    elif cmd == 0x5A:  # ld e,d
        print('ld e,d')
        i += 1

    elif cmd == 0x5B:  # ld e,e
        print('ld e,e')
        i += 1

    elif cmd == 0x5C:  # ld e,h
        print('ld e,h')
        i += 1

    elif cmd == 0x5D:  # ld e,l
        print('ld e,l')
        i += 1

    elif cmd == 0x5E:  # ld e,(hl)
        print('ld e,(hl)')
        i += 1

    elif cmd == 0x5F:  # ld e,a
        print('ld e,a')
        i += 1

    elif cmd == 0x60:  # ld h,b
        print('ld h,b')
        i += 1

    elif cmd == 0x61:  # ld h,c
        print('ld h,c')
        i += 1

    elif cmd == 0x62:  # ld h,d
        print('ld h,d')
        i += 1

    elif cmd == 0x63:  # ld h,e
        print('ld h,e')
        i += 1

    elif cmd == 0x64:  # ld h,h
        print('ld h,h')
        i += 1

    elif cmd == 0x65:  # ld h,l
        print('ld h,l')
        i += 1

    elif cmd == 0x66:  # ld h,(hl)
        print('ld h,(hl)')
        i += 1

    elif cmd == 0x67:  # ld h,a
        print('ld h,a')
        i += 1

    elif cmd == 0x68:  # ld l,b
        print('ld l,b')
        i += 1

    elif cmd == 0x69:  # ld l,c
        print('ld l,c')
        i += 1

    elif cmd == 0x6A:  # ld l,d
        print('ld l,d')
        i += 1

    elif cmd == 0x6B:  # ld l,e
        print('ld l,e')
        i += 1

    elif cmd == 0x6C:  # ld l,h
        print('ld l,h')
        i += 1

    elif cmd == 0x6D:  # ld l,l
        print('ld l,l')
        i += 1

    elif cmd == 0x6E:  # ld l,(hl)
        print('ld l,(hl)')
        i += 1

    elif cmd == 0x6F:  # ld l,a
        print('ld l,a')
        i += 1

    elif cmd == 0x70:  # ld (hl),b
        print('ld (hl),b')
        i += 1

    elif cmd == 0x71:  # ld (hl),c
        print('ld (hl),c')
        i += 1

    elif cmd == 0x72:  # ld (hl),d
        print('ld (hl),d')
        i += 1

    elif cmd == 0x73:  # ld (hl),e
        print('ld (hl),e')
        i += 1

    elif cmd == 0x74:  # ld (hl),h
        print('ld (hl),h')
        i += 1

    elif cmd == 0x75:  # ld (hl),l
        print('ld (hl),l')
        i += 1

    elif cmd == 0x76:  # halt
        print('halt')
        i += 1

    elif cmd == 0x77:  # ld (hl),a
        print('ld (hl),a')
        i += 1

    elif cmd == 0x78:  # ld a,b
        print('ld a,b')
        i += 1

    elif cmd == 0x79:  # ld a,c
        print('ld a,c')
        i += 1

    elif cmd == 0x7A:  # ld a,d
        print('ld a,d')
        i += 1

    elif cmd == 0x7B:  # ld a,e
        print('ld a,e')
        i += 1

    elif cmd == 0x7C:  # ld a,h
        print('ld a,h')
        i += 1

    elif cmd == 0x7D:  # ld a,l
        print('ld a,l')
        i += 1

    elif cmd == 0x7E:  # ld a,(hl)
        print('ld a,(hl)')
        i += 1

    elif cmd == 0x7F:  # ld a,a
        print('ld a,a')
        i += 1

    elif cmd == 0x80:  # add a,b
        print('add a,b')
        i += 1

    elif cmd == 0x81:  # add a,c
        print('add a,c')
        i += 1

    elif cmd == 0x82:  # add a,d
        print('add a,d')
        i += 1

    elif cmd == 0x83:  # add a,e
        print('add a,e')
        i += 1

    elif cmd == 0x84:  # add a,h
        print('add a,h')
        i += 1

    elif cmd == 0x85:  # add a,l
        print('add a,l')
        i += 1

    elif cmd == 0x86:  # add a,(hl)
        print('add a,(hl)')
        i += 1

    elif cmd == 0x87:  # add a,a
        print('add a,a')
        i += 1

    elif cmd == 0x88:  # adc a,b
        print('adc a,b')
        i += 1

    elif cmd == 0x89:  # adc a,c
        print('adc a,c')
        i += 1

    elif cmd == 0x8A:  # adc a,d
        print('adc a,d')
        i += 1

    elif cmd == 0x8B:  # adc a,e
        print('adc a,e')
        i += 1

    elif cmd == 0x8C:  # adc a,h
        print('adc a,h')
        i += 1

    elif cmd == 0x8D:  # adc a,l
        print('adc a,l')
        i += 1

    elif cmd == 0x8E:  # adc a,(hl)
        print('adc a,(hl)')
        i += 1

    elif cmd == 0x8F:  # adc a,a
        print('adc a,a')
        i += 1

    elif cmd == 0x90:  # sub b
        print('sub b')
        i += 1

    elif cmd == 0x91:  # sub c
        print('sub c')
        i += 1

    elif cmd == 0x92:  # sub d
        print('sub d')
        i += 1

    elif cmd == 0x93:  # sub e
        print('sub e')
        i += 1

    elif cmd == 0x94:  # sub h
        print('sub h')
        i += 1

    elif cmd == 0x95:  # sub l
        print('sub l')
        i += 1

    elif cmd == 0x96:  # sub (hl)
        print('sub (hl)')
        i += 1

    elif cmd == 0x97:  # sub a
        print('sub a')
        i += 1

    elif cmd == 0x98:  # sbc a,b
        print('sbc a,b')
        i += 1

    elif cmd == 0x99:  # sbc a,c
        print('sbc a,c')
        i += 1

    elif cmd == 0x9A:  # sbc a,d
        print('sbc a,d')
        i += 1

    elif cmd == 0x9B:  # sbc a,e
        print('sbc a,e')
        i += 1

    elif cmd == 0x9C:  # sbc a,h
        print('sbc a,h')
        i += 1

    elif cmd == 0x9D:  # sbc a,l
        print('sbc a,l')
        i += 1

    elif cmd == 0x9E:  # sbc a,(hl)
        print('sbc a,(hl)')
        i += 1

    elif cmd == 0x9F:  # sbc a,a
        print('sbc a,a')
        i += 1

    elif cmd == 0xA0:  # and b
        print('and b')
        i += 1

    elif cmd == 0xA1:  # and c
        print('and c')
        i += 1

    elif cmd == 0xA2:  # and d
        print('and d')
        i += 1

    elif cmd == 0xA3:  # and e
        print('and e')
        i += 1

    elif cmd == 0xA4:  # and h
        print('and h')
        i += 1

    elif cmd == 0xA5:  # and l
        print('and l')
        i += 1

    elif cmd == 0xA6:  # and (hl)
        print('and (hl)')
        i += 1

    elif cmd == 0xA7:  # and a
        print('and a')
        i += 1

    elif cmd == 0xA8:  # xor b
        print('xor b')
        i += 1

    elif cmd == 0xA9:  # xor c
        print('xor c')
        i += 1

    elif cmd == 0xAA:  # xor d
        print('xor d')
        i += 1

    elif cmd == 0xAB:  # xor e
        print('xor e')
        i += 1

    elif cmd == 0xAC:  # xor h
        print('xor h')
        i += 1

    elif cmd == 0xAD:  # xor l
        print('xor l')
        i += 1

    elif cmd == 0xAE:  # xor (hl)
        print('xor (hl)')
        i += 1

    elif cmd == 0xAF:  # xor a
        print('xor a')
        i += 1

    elif cmd == 0xB0:  # or b
        print('or b')
        i += 1

    elif cmd == 0xB1:  # or c
        print('or c')
        i += 1

    elif cmd == 0xB2:  # or d
        print('or d')
        i += 1

    elif cmd == 0xB3:  # or e
        print('or e')
        i += 1

    elif cmd == 0xB4:  # or h
        print('or h')
        i += 1

    elif cmd == 0xB5:  # or l
        print('or l')
        i += 1

    elif cmd == 0xB6:  # or (hl)
        print('or (hl)')
        i += 1

    elif cmd == 0xB7:  # or a
        print('or a')
        i += 1

    elif cmd == 0xB8:  # cp b
        print('cp b')
        i += 1

    elif cmd == 0xB9:  # cp c
        print('cp c')
        i += 1

    elif cmd == 0xBA:  # cp d
        print('cp d')
        i += 1

    elif cmd == 0xBB:  # cp e
        print('cp e')
        i += 1

    elif cmd == 0xBC:  # cp h
        print('cp h')
        i += 1

    elif cmd == 0xBD:  # cp l
        print('cp l')
        i += 1

    elif cmd == 0xBE:  # cp (hl)
        print('cp (hl)')
        i += 1

    elif cmd == 0xBF:  # cp a
        print('cp a')
        i += 1

    elif cmd == 0xC0:  # ret nz
        print('ret nz')
        i += 1

    elif cmd == 0xC1:  # pop bc
        print('pop bc')
        i += 1

    elif cmd == 0xC2:  # jp nz,$xxyy
        nextbytes = bytestream[i+1:i+3]
        print('jp nz,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xC3:  # jp $xxyy
        nextbytes = bytestream[i+1:i+3]
        print('jp $%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xC4:  # call nz,$xxyy
        nextbytes = bytestream[i+1:i+3]
        print('call nz,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xC5:  # push bc
        print('push bc')
        i += 1

    elif cmd == 0xC6:  # add a,$xx
        nextbytes = bytestream[i+1:i+2]
        print('add a,$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xC7:  # rst $00
        print('rst $00')
        i += 1

    elif cmd == 0xC8:  # ret z
        print('ret z')
        i += 1

    elif cmd == 0xC9:  # ret
        print('ret')
        i += 1

    elif cmd == 0xCA:  # jp z,$xxyy
        nextbytes = bytestream[i+1:i+3]
        print('jp nz,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xCB:  # rlc b
        nextbytes = bytestream[i+1:i+2]
        if nextbytes[0] == 0x00:
            print('rlc b')
        elif nextbytes[0] == 0x01:
            print('rlc c')
        elif nextbytes[0] == 0x02:
            print('rlc d')
        elif nextbytes[0] == 0x03:
            print('rlc e')
        elif nextbytes[0] == 0x04:
            print('rlc h')
        elif nextbytes[0] == 0x05:
            print('rlc l')
        elif nextbytes[0] == 0x06:
            print('rlc (hl)')
        elif nextbytes[0] == 0x07:
            print('rlc a')
        elif nextbytes[0] == 0x08:
            print('rrc b')
        elif nextbytes[0] == 0x09:
            print('rrc c')
        elif nextbytes[0] == 0x0A:
            print('rrc d')
        elif nextbytes[0] == 0x0B:
            print('rrc e')
        elif nextbytes[0] == 0x0C:
            print('rrc h')
        elif nextbytes[0] == 0x0D:
            print('rrc l')
        elif nextbytes[0] == 0x0E:
            print('rrc (hl)')
        elif nextbytes[0] == 0x0F:
            print('rrc a')
        elif nextbytes[0] == 0x10:
            print('rl b')
        elif nextbytes[0] == 0x11:
            print('rl c')
        elif nextbytes[0] == 0x12:
            print('rl d')
        elif nextbytes[0] == 0x13:
            print('rl e')
        elif nextbytes[0] == 0x14:
            print('rl h')
        elif nextbytes[0] == 0x15:
            print('rl l')
        elif nextbytes[0] == 0x16:
            print('rl (hl)')
        elif nextbytes[0] == 0x17:
            print('rl a')
        elif nextbytes[0] == 0x18:
            print('rr b')
        elif nextbytes[0] == 0x19:
            print('rr c')
        elif nextbytes[0] == 0x1A:
            print('rr d')
        elif nextbytes[0] == 0x1B:
            print('rr e')
        elif nextbytes[0] == 0x1C:
            print('rr h')
        elif nextbytes[0] == 0x1D:
            print('rr l')
        elif nextbytes[0] == 0x1E:
            print('rr (hl)')
        elif nextbytes[0] == 0x1F:
            print('rr a')
        elif nextbytes[0] == 0x20:
            print('sla b')
        elif nextbytes[0] == 0x21:
            print('sla c')
        elif nextbytes[0] == 0x22:
            print('sla d')
        elif nextbytes[0] == 0x23:
            print('sla e')
        elif nextbytes[0] == 0x24:
            print('sla h')
        elif nextbytes[0] == 0x25:
            print('sla l')
        elif nextbytes[0] == 0x26:
            print('sla (hl)')
        elif nextbytes[0] == 0x27:
            print('sla a')
        elif nextbytes[0] == 0x28:
            print('sra b')
        elif nextbytes[0] == 0x29:
            print('sra c')
        elif nextbytes[0] == 0x2A:
            print('sra d')
        elif nextbytes[0] == 0x2B:
            print('sra')
        elif nextbytes[0] == 0x2C:
            print('sra h')
        elif nextbytes[0] == 0x2D:
            print('sra l')
        elif nextbytes[0] == 0x2E:
            print('sra (hl)')
        elif nextbytes[0] == 0x2F:
            print('sra a')
        elif nextbytes[0] == 0x30:
            print('swap b')
        elif nextbytes[0] == 0x31:
            print('swap c')
        elif nextbytes[0] == 0x32:
            print('swap d')
        elif nextbytes[0] == 0x33:
            print('swap e')
        elif nextbytes[0] == 0x34:
            print('swap h')
        elif nextbytes[0] == 0x35:
            print('swap l')
        elif nextbytes[0] == 0x36:
            print('swap (hl)')
        elif nextbytes[0] == 0x37:
            print('swap a')
        elif nextbytes[0] == 0x38:
            print('srl b')
        elif nextbytes[0] == 0x39:
            print('srl c')
        elif nextbytes[0] == 0x3A:
            print('srl d')
        elif nextbytes[0] == 0x3B:
            print('srl e')
        elif nextbytes[0] == 0x3C:
            print('srl h')
        elif nextbytes[0] == 0x3D:
            print('srl l')
        elif nextbytes[0] == 0x3E:
            print('srl (hl)')
        elif nextbytes[0] == 0x3F:
            print('srl a')
        elif nextbytes[0] == 0x40:
            print('bit 0,b')
        elif nextbytes[0] == 0x41:
            print('bit 0,c')
        elif nextbytes[0] == 0x42:
            print('bit 0,d')
        elif nextbytes[0] == 0x43:
            print('bit 0,e')
        elif nextbytes[0] == 0x44:
            print('bit 0,h')
        elif nextbytes[0] == 0x45:
            print('bit 0,l')
        elif nextbytes[0] == 0x46:
            print('bit 0,(hl)')
        elif nextbytes[0] == 0x47:
            print('bit 0,a')
        elif nextbytes[0] == 0x48:
            print('bit 1,b')
        elif nextbytes[0] == 0x49:
            print('bit 1,c')
        elif nextbytes[0] == 0x4A:
            print('bit 1,d')
        elif nextbytes[0] == 0x4B:
            print('bit 1,e')
        elif nextbytes[0] == 0x4C:
            print('bit 1,h')
        elif nextbytes[0] == 0x4D:
            print('bit 1,l')
        elif nextbytes[0] == 0x4E:
            print('bit 1,(hl)')
        elif nextbytes[0] == 0x4F:
            print('bit 1,a')
        elif nextbytes[0] == 0x50:
            print('bit 2,b')
        elif nextbytes[0] == 0x51:
            print('bit 2,c')
        elif nextbytes[0] == 0x52:
            print('bit 2,d')
        elif nextbytes[0] == 0x53:
            print('bit 2,e')
        elif nextbytes[0] == 0x54:
            print('bit 2,h')
        elif nextbytes[0] == 0x55:
            print('bit 2,l')
        elif nextbytes[0] == 0x56:
            print('bit 2,(hl)')
        elif nextbytes[0] == 0x57:
            print('bit 2,a')
        elif nextbytes[0] == 0x58:
            print('bit 3,b')
        elif nextbytes[0] == 0x59:
            print('bit 3,c')
        elif nextbytes[0] == 0x5A:
            print('bit 3,d')
        elif nextbytes[0] == 0x5B:
            print('bit 3,e')
        elif nextbytes[0] == 0x5C:
            print('bit 3,h')
        elif nextbytes[0] == 0x5D:
            print('bit 3,l')
        elif nextbytes[0] == 0x5E:
            print('bit 3,(hl)')
        elif nextbytes[0] == 0x5F:
            print('bit 3,a')
        elif nextbytes[0] == 0x60:
            print('bit 4,b')
        elif nextbytes[0] == 0x61:
            print('bit 4,c')
        elif nextbytes[0] == 0x62:
            print('bit 4,d')
        elif nextbytes[0] == 0x63:
            print('bit 4,e')
        elif nextbytes[0] == 0x64:
            print('bit 4,h')
        elif nextbytes[0] == 0x65:
            print('bit 4,l')
        elif nextbytes[0] == 0x66:
            print('bit 4,(hl)')
        elif nextbytes[0] == 0x67:
            print('bit 4,a')
        elif nextbytes[0] == 0x68:
            print('bit 5,b')
        elif nextbytes[0] == 0x69:
            print('bit 5,c')
        elif nextbytes[0] == 0x6A:
            print('bit 5,d')
        elif nextbytes[0] == 0x6B:
            print('bit 5,e')
        elif nextbytes[0] == 0x6C:
            print('bit 5,h')
        elif nextbytes[0] == 0x6D:
            print('bit 5,l')
        elif nextbytes[0] == 0x6E:
            print('bit 5,(hl)')
        elif nextbytes[0] == 0x6F:
            print('bit 5,a')
        elif nextbytes[0] == 0x70:
            print('bit 6,b')
        elif nextbytes[0] == 0x71:
            print('bit 6,c')
        elif nextbytes[0] == 0x72:
            print('bit 6,d')
        elif nextbytes[0] == 0x73:
            print('bit 6,e')
        elif nextbytes[0] == 0x74:
            print('bit 6,h')
        elif nextbytes[0] == 0x75:
            print('bit 6,l')
        elif nextbytes[0] == 0x76:
            print('bit 6,(hl)')
        elif nextbytes[0] == 0x77:
            print('bit 6,a')
        elif nextbytes[0] == 0x78:
            print('bit 7,b')
        elif nextbytes[0] == 0x79:
            print('bit 7,c')
        elif nextbytes[0] == 0x7A:
            print('bit 7,d')
        elif nextbytes[0] == 0x7B:
            print('bit 7,e')
        elif nextbytes[0] == 0x7C:
            print('bit 7,h')
        elif nextbytes[0] == 0x7D:
            print('bit 7,(hl)')
        elif nextbytes[0] == 0x7F:
            print('bit 7,a')
        elif nextbytes[0] == 0x80:
            print('res 0,b')
        elif nextbytes[0] == 0x81:
            print('res 0,c')
        elif nextbytes[0] == 0x82:
            print('res 0,d')
        elif nextbytes[0] == 0x83:
            print('res 0,e')
        elif nextbytes[0] == 0x84:
            print('res 0,h')
        elif nextbytes[0] == 0x85:
            print('res 0,l')
        elif nextbytes[0] == 0x86:
            print('res 0,(hl)')
        elif nextbytes[0] == 0x87:
            print('res 0,a')
        elif nextbytes[0] == 0x88:
            print('res 1,b')
        elif nextbytes[0] == 0x89:
            print('res 1,c')
        elif nextbytes[0] == 0x8A:
            print('res 1,d')
        elif nextbytes[0] == 0x8B:
            print('res 1,e')
        elif nextbytes[0] == 0x8C:
            print('res 1,h')
        elif nextbytes[0] == 0x8D:
            print('res 1,l')
        elif nextbytes[0] == 0x8E:
            print('res 1,(hl)')
        elif nextbytes[0] == 0x8F:
            print('res 1,a')
        elif nextbytes[0] == 0x90:
            print('res 2,b')
        elif nextbytes[0] == 0x91:
            print('res 2,c')
        elif nextbytes[0] == 0x92:
            print('res 2,d')
        elif nextbytes[0] == 0x93:
            print('res 2,e')
        elif nextbytes[0] == 0x94:
            print('res 2,h')
        elif nextbytes[0] == 0x95:
            print('res 2,l')
        elif nextbytes[0] == 0x96:
            print('res 2,(hl)')
        elif nextbytes[0] == 0x97:
            print('res 2,a')
        elif nextbytes[0] == 0x98:
            print('res 3,b')
        elif nextbytes[0] == 0x99:
            print('res 3,c')
        elif nextbytes[0] == 0x9A:
            print('res 3,d')
        elif nextbytes[0] == 0x9B:
            print('res 3,e')
        elif nextbytes[0] == 0x9C:
            print('res 3,h')
        elif nextbytes[0] == 0x9D:
            print('res 3,l')
        elif nextbytes[0] == 0x9E:
            print('res 3,(hl)')
        elif nextbytes[0] == 0x9F:
            print('res 3,a')
        elif nextbytes[0] == 0xA0:
            print('res 4,b')
        elif nextbytes[0] == 0xA1:
            print('res 4,c')
        elif nextbytes[0] == 0xA2:
            print('res 4,d')
        elif nextbytes[0] == 0xA3:
            print('res 4,e')
        elif nextbytes[0] == 0xA4:
            print('res 4,h')
        elif nextbytes[0] == 0xA5:
            print('res 4,l')
        elif nextbytes[0] == 0xA6:
            print('res 4,(hl)')
        elif nextbytes[0] == 0xA7:
            print('res 4,a')
        elif nextbytes[0] == 0xA8:
            print('res 5,b')
        elif nextbytes[0] == 0xA9:
            print('res 5,c')
        elif nextbytes[0] == 0xAA:
            print('res 5,d')
        elif nextbytes[0] == 0xAB:
            print('res 5,e')
        elif nextbytes[0] == 0xAC:
            print('res 5,h')
        elif nextbytes[0] == 0xAD:
            print('res 5,l')
        elif nextbytes[0] == 0xAE:
            print('res 5,(hl)')
        elif nextbytes[0] == 0xAf:
            print('res 5,a')
        elif nextbytes[0] == 0xB0:
            print('res 6,b')
        elif nextbytes[0] == 0xB1:
            print('res 6,c')
        elif nextbytes[0] == 0xB2:
            print('res 6,d')
        elif nextbytes[0] == 0xB3:
            print('res 6,e')
        elif nextbytes[0] == 0xB4:
            print('res 6,h')
        elif nextbytes[0] == 0xB5:
            print('res 6,l')
        elif nextbytes[0] == 0xB6:
            print('res 6,(hl)')
        elif nextbytes[0] == 0xB7:
            print('res 6,a')
        elif nextbytes[0] == 0xB8:
            print('res 7,b')
        elif nextbytes[0] == 0xB9:
            print('res 7,c')
        elif nextbytes[0] == 0xBA:
            print('res 7,d')
        elif nextbytes[0] == 0xBB:
            print('res 7,e')
        elif nextbytes[0] == 0xBc:
            print('res 7,h')
        elif nextbytes[0] == 0xBD:
            print('res 7,l')
        elif nextbytes[0] == 0xBE:
            print('res 7,(hl)')
        elif nextbytes[0] == 0xBF:
            print('res 7,a')
        elif nextbytes[0] == 0xC0:
            print('set 0,b')
        elif nextbytes[0] == 0xC1:
            print('set 0,c')
        elif nextbytes[0] == 0xC2:
            print('set 0,d')
        elif nextbytes[0] == 0xC3:
            print('set 0,e')
        elif nextbytes[0] == 0xC4:
            print('set 0,h')
        elif nextbytes[0] == 0xC5:
            print('set 0,l')
        elif nextbytes[0] == 0xC6:
            print('set 0,(hl)')
        elif nextbytes[0] == 0xC7:
            print('set 0,a')
        elif nextbytes[0] == 0xC8:
            print('set 1,b')
        elif nextbytes[0] == 0xC9:
            print('set 1,c')
        elif nextbytes[0] == 0xCA:
            print('set 1,d')
        elif nextbytes[0] == 0xCB:
            print('set 1,e')
        elif nextbytes[0] == 0xCC:
            print('set 1,h')
        elif nextbytes[0] == 0xCD:
            print('set 1,l')
        elif nextbytes[0] == 0xCE:
            print('set 1,(hl)')
        elif nextbytes[0] == 0xCF:
            print('set 1,a')
        elif nextbytes[0] == 0xD0:
            print('set 2,b')
        elif nextbytes[0] == 0xD1:
            print('set 2,c')
        elif nextbytes[0] == 0xD2:
            print('set 2,d')
        elif nextbytes[0] == 0xD3:
            print('set 2,e')
        elif nextbytes[0] == 0xD4:
            print('set 2,h')
        elif nextbytes[0] == 0xD5:
            print('set 2,l')
        elif nextbytes[0] == 0xD6:
            print('set 2,(hl)')
        elif nextbytes[0] == 0xD7:
            print('set 2,a')
        elif nextbytes[0] == 0xD8:
            print('set 3,b')
        elif nextbytes[0] == 0xD9:
            print('set 3,c')
        elif nextbytes[0] == 0xDA:
            print('set 3,d')
        elif nextbytes[0] == 0xDB:
            print('set 3,e')
        elif nextbytes[0] == 0xDC:
            print('set 3,h')
        elif nextbytes[0] == 0xDD:
            print('set 3,l')
        elif nextbytes[0] == 0xDE:
            print('set 3,(hl)')
        elif nextbytes[0] == 0xDF:
            print('set 3,a')
        elif nextbytes[0] == 0xE0:
            print('set 4,b')
        elif nextbytes[0] == 0xE1:
            print('set 4,c')
        elif nextbytes[0] == 0xE2:
            print('set 4,d')
        elif nextbytes[0] == 0xE3:
            print('set 4,e')
        elif nextbytes[0] == 0xE4:
            print('set 4,h')
        elif nextbytes[0] == 0xE5:
            print('set 4,l')
        elif nextbytes[0] == 0xE6:
            print('set 4,(hl)')
        elif nextbytes[0] == 0xE7:
            print('set 4,a')
        elif nextbytes[0] == 0xE8:
            print('set 5,b')
        elif nextbytes[0] == 0xE9:
            print('set 5,c')
        elif nextbytes[0] == 0xEA:
            print('set 5,d')
        elif nextbytes[0] == 0xEB:
            print('set 5,e')
        elif nextbytes[0] == 0xEC:
            print('set 5,h')
        elif nextbytes[0] == 0xED:
            print('set 5,l')
        elif nextbytes[0] == 0xEE:
            print('set 5,(hl)')
        elif nextbytes[0] == 0xEF:
            print('set 5,a')
        elif nextbytes[0] == 0xF0:
            print('set 6,b')
        elif nextbytes[0] == 0xF1:
            print('set 6,c')
        elif nextbytes[0] == 0xF2:
            print('set 6,d')
        elif nextbytes[0] == 0xF3:
            print('set 6,e')
        elif nextbytes[0] == 0xF4:
            print('set 6,h')
        elif nextbytes[0] == 0xF5:
            print('set 6,l')
        elif nextbytes[0] == 0xF6:
            print('set 6,(hl)')
        elif nextbytes[0] == 0xF7:
            print('set 6,a')
        elif nextbytes[0] == 0xF8:
            print('set 7,b')
        elif nextbytes[0] == 0xF9:
            print('set 7,c')
        elif nextbytes[0] == 0xFA:
            print('set 7,d')
        elif nextbytes[0] == 0xFB:
            print('set 7,e')
        elif nextbytes[0] == 0xFC:
            print('set 7,h')
        elif nextbytes[0] == 0xFD:
            print('set 7,l')
        elif nextbytes[0] == 0xFE:
            print('set 7,(hl)')
        elif nextbytes[0] == 0xFF:    
            print('set 7,a')
        i += 2

    elif cmd == 0xCC:  # call z,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('call z,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xCD:  # call $aabb
        nextbytes = bytestream[i+1:i+3]
        print('call $%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xCE:  # adc a,$xx
        nextbytes = bytestream[i+1:i+2]
        print('adc a,$%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xCF:  # rst $08
        print('rst $08')
        i += 1

    elif cmd == 0xD0:  # ret nc
        print('ret nc')
        i += 1

    elif cmd == 0xD1:  # pop de
        print('pop de')
        i += 1

    elif cmd == 0xD2:  # jp nc,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('jp nc,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xD4:  # call nc,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('call nc,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xD5:  # push de
        print('push de')
        i += 1

    elif cmd == 0xD6:  # sub $xx
        nextbytes = bytestream[i+1:i+2]
        print('sub $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xD7:  # rst $10
        print('rst $10')
        i += 1

    elif cmd == 0xD8:  # ret c
        print('ret c')
        i += 1

    elif cmd == 0xD9:  # reti
        print('reti')
        i += 1

    elif cmd == 0xDA:  # jp c,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('jp c,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xDC:  # call c,$aabb
        nextbytes = bytestream[i+1:i+3]
        print('call c,$%s%s' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xDE:  # sbc a,$xx
        nextbytes = bytestream[i+1:i+2]
        print('sbc $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xDF:  # rst $18
        print('rst $18')
        i += 1

    elif cmd == 0xE0:  # ld [$FFxx],a
        nextbytes = bytestream[i+1:i+2]
        print('ld [$FF%s],a' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xE1:  # pop hl
        print('pop hl')
        i += 1

    elif cmd == 0xE2:  # ld (c),a
        print('ld (c),a')
        i += 1

    elif cmd == 0xE5:  # push hl
        print('push hl')
        i += 1

    elif cmd == 0xE6:  # and $xx
        nextbytes = bytestream[i+1:i+2]
        print('and $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xE7:  # rst $20
        print('rst $20')
        i += 1

    elif cmd == 0xE8:  # add sp,xx
        nextbytes = bytestream[i+1:i+2]
        print('add sp,%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xE9:  # jp (hl)
        print('jp (hl)')
        i += 1

    elif cmd == 0xEA:  # ld ($xxyy),a
        nextbytes = bytestream[i+1:i+3]
        print('ld ($%s%s),a' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xEE:  # xor $xx
        nextbytes = bytestream[i+1:i+2]
        print('xor $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xEF:  # rst $28
        print('rst $28')
        i += 1

    elif cmd == 0xF0:  # ld a,[$FFxx]
        nextbytes = bytestream[i+1:i+2]
        print('ld a,[$FF%s]' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xF1:  # pop af
        print('pop af')
        i += 1

    elif cmd == 0xF2:  # ld a,(c)
        print('ld a,(c)')
        i += 1

    elif cmd == 0xF3:  # di
        print('di')
        i += 1

    elif cmd == 0xF5:  # push af
        print('push af')
        i += 1

    elif cmd == 0xF6:  # or $xx
        nextbytes = bytestream[i+1:i+2]
        print('or $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xF7:  # rst $30
        print('rst $30')
        i += 1

    elif cmd == 0xF8:  # ld hl,sp
        print('ld hl,sp')
        i += 1

    elif cmd == 0xF9:  # ld sp,hl
        print('ld sp,hl')
        i += 1

    elif cmd == 0xFA:  # ld a,($xxyy)
        nextbytes = bytestream[i+1:i+3]
        print('ld a,($%s%s)' % (hex(nextbytes[1])[2:].zfill(2), hex(nextbytes[0])[2:].zfill(2)))
        i += 3

    elif cmd == 0xFB:  # ei
        print('ei')
        i += 1

    elif cmd == 0xFE:  # cp $xx
        nextbytes = bytestream[i+1:i+2]
        print('cp $%s' % hex(nextbytes[0])[2:].zfill(2))
        i += 2

    elif cmd == 0xFF:  # rst $38
        print('rst $38')
        i += 1

    else:
        print('Unrecognised opcode.')
