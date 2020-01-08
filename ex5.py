name = 'Zed A. Shaw'
age = 35  # not a lie
imperial_height = 74  # inches
metric_height = imperial_height * 2.54  # centimeters
imperial_weight = 180  # lbs
metric_weight = imperial_weight * 0.453592  # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {imperial_height} inches or {metric_height} centimeters all.")
print(f"He's {imperial_weight} pounds or {metric_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
imperial_total = age + imperial_height + imperial_weight
print(f"If I add {age}, {imperial_height}, and {imperial_weight} I get {imperial_total}.")
metric_total = age + metric_height + metric_weight
print(f"If I add {age}, {metric_height}, and {metric_weight} I get {metric_total}.")

# Practicing round
imperial_total_rounded = round(imperial_total, 2)
metric_total_rounded = round(metric_total, 2)
print(f"Imperial total rounded {imperial_total_rounded}.")
print(f"Metric total rounded {round(metric_total, 2)}.")
