import tkinter
import vlajkamodul

# nacitaj data
krajiny_data = {}
with open('modul_s_triedou/krajiny.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('|')
        if len(parts) == 6:
            name, zvislo_str, colors_str, area_str, pop_str, gdp_str = parts
            zvislo = zvislo_str.lower() == 'true'
            farby = [c.strip() for c in colors_str.split(',')]
            krajiny_data[name] = {
                'zvislo': zvislo,
                'farby': farby,
                'area': float(area_str),
                'pop': float(pop_str),
                'gdp': float(gdp_str)
            }

# GUI
root = tkinter.Tk()
root.title('Vlajky krajin')

canvas = tkinter.Canvas(root, width=1200, height=600, bg='lightgray')
canvas.pack(pady=10)

# tlacidla
frame = tkinter.Frame(root)
frame.pack()

criteria = ['Rozloha', 'Obyvatelia', 'HDP', 'Hustota']

var = tkinter.StringVar(value=criteria[0])
for crit in criteria:
    tkinter.Radiobutton(frame, text=crit, variable=var, value=crit, command=lambda: update_sizes()).pack(side=tkinter.LEFT)

# vytvor vlajky
vlajky = []
base_sirka = 100
base_vyska = 60
for name, data in krajiny_data.items():
    vlajka = vlajkamodul.Vlajka(0, 0, base_sirka, base_vyska, data['zvislo'], data['farby'])  # Russia
    vlajky.append((vlajka, name, data))

current_scales = {name: 1.0 for name in krajiny_data}

def get_criterion_data(crit):
    if crit == 'Rozloha':
        return {name: data['area'] for name, data in krajiny_data.items()}
    elif crit == 'Obyvatelia':
        return {name: data['pop'] for name, data in krajiny_data.items()}
    elif crit == 'HDP':
        return {name: data['gdp'] for name, data in krajiny_data.items()}
    elif crit == 'Hustota':
        return {name: data['pop']/data['area'] if data['area'] > 0 else 0 for name, data in krajiny_data.items()}

def update_sizes():
    crit = var.get()
    data = get_criterion_data(crit)
    if not data:
        return
    values = list(data.values())
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val:
        return
    
    # Vyčisti canvas
    canvas.delete("all")
    
# zorad vlajky
    sorted_vlajky = sorted(vlajky, key=lambda item: data[item[1]], reverse=True)
    
    x_start = 50
    y_center = 300
    spacing = 20
    current_x = x_start
    for vlajka, name, _ in sorted_vlajky:
        val = data[name]
        scale_factor = 0.5 + 1.5 * (val - min_val) / (max_val - min_val)
        target_rel = scale_factor
        current_rel = current_scales[name]
        zoom_pomer = target_rel / current_rel
        vlajka.zoom(zoom_pomer)
        current_scales[name] = target_rel
        
# nova pozicia
        sirka = vlajka.sirka
        vlajka.x = current_x + sirka / 2
        vlajka.y = y_center
        
        vlajka.kresli(canvas)
        current_x += sirka + spacing

# prve zobrazenie
for v, _, _ in vlajky:
    v.kresli(canvas)

root.mainloop()
