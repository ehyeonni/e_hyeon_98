#########################################################################
### Date: 2017/11/9
### file name: tracingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
#########################################################################

# =======================================================================
# import needed library
# =======================================================================
import getLine
import movement


def line_tracing():
    while True:
        movement.pwm_setup()
        line_check = getLine.get_line()
        if line_check == ['1', '1', '1', '1', '1']:
            movement.go_forward_infinite(70, 70, line_check)
        elif line_check == ['0', '1', '1', '1', '1']:
            movement.go_forward_infinite(15, 100, line_check)
        elif line_check == ['1', '0', '1', '1', '1']:
            movement.go_forward_infinite(30, 70, line_check)
        elif line_check == ['1', '1', '0', '1', '1']:
            movement.go_forward_infinite(70, 70, line_check)
        elif line_check == ['1', '1', '1', '0', '1']:
            movement.go_forward_infinite(70, 30, line_check)
        elif line_check == ['1', '1', '1', '1', '0']:
            movement.go_forward_infinite(100, 15, line_check)
        elif line_check == ['0', '0', '1', '1', '1']:
            movement.go_forward_infinite(15, 90, line_check)
        elif line_check == ['1', '0', '0', '1', '1']:
            movement.go_forward_infinite(30, 90, line_check)
        elif line_check == ['1', '1', '0', '0', '1']:
            movement.go_forward_infinite(90, 30, line_check)
        elif line_check == ['1', '1', '1', '0', '0']:
            movement.go_forward_infinite(90, 10, line_check)
        elif line_check == ['0', '0', '0', '1', '1']:
            movement.go_forward_infinite(15, 90, line_check)
        elif line_check == ['1', '0', '0', '0', '1']:
            movement.go_forward_infinite(70, 70, line_check)
        elif line_check == ['1', '1', '0', '0', '0']:
            movement.go_forward_infinite(90, 10, line_check)
        elif line_check == ['0', '0', '0', '0', '1']:
            movement.go_forward_infinite(60, 70, line_check)
        elif line_check == ['1', '0', '0', '0', '0']:
            movement.go_forward_infinite(70, 60, line_check)
