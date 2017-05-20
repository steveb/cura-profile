M136 (enable build)
M73 P0
M135 T0
M104 S220 T0
M133 T0
G162 X Y F2000(home XY axes maximum)
G161 Z F900(home Z axis minimum)
G92 X0 Y0 Z-5 A0 B0 (set Z to -5)
G1 Z0.0 F{travel_speed}(move Z to '0')
G161 Z F100(home Z axis minimum)
M132 X Y Z A B (Recall stored home offsets for XYZAB axis)
; G92 X152 Y72 Z0 A0 B0
G1 X-112 Y-72 Z40 F{travel_speed} (move to waiting position)
G130 X20 Y20 A20 B20 (Lower stepper Vrefs while heating)
G130 X127 Y127 A127 B127 (Set Stepper motor Vref to defaults)
M73 P0;
