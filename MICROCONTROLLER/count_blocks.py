import sys
sys.path.append('a:\\SEM4_Complete\\MICROCONTROLLER')
import generate_unit_modes

data = generate_unit_modes.UNIT_MODES_DATA
for k, v in data.items():
    t_m1 = v["mode1"].count('class="topic-block"') + v["mode1"].count("class='topic-block'")
    t_m2 = v["mode2"].count('class="topic-block"') + v["mode2"].count("class='topic-block'")
    q_m3 = v["mode3"].count('class="pyq-solved"') + v["mode3"].count("class='pyq-solved'")
    print(f"Unit {k}: Precise Mode 1 Topics = {t_m1}, Precise Mode 2 Topics = {t_m2}, Precise Mode 3 Solved Qs = {q_m3}")
