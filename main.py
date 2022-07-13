def on_received_number(receivedNumber):
    global item
    item = receivedNumber
    if item == 0:
        maqueen.motor_stop(maqueen.Motors.ALL)
    if item == 1:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
    if item == 2:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
    if item == 3:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    if item == 4:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
radio.on_received_number(on_received_number)

item = 0
radio.set_group(1)