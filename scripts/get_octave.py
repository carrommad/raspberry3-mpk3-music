import mido
for p in mido.get_input_names():
    if 'mpk' in p.lower() or 'akai' in p.lower():
        inport = mido.open_input(p)
        print('LISTENING')
        msg = inport.receive()
        print('NOTE:', msg.note)
        break
