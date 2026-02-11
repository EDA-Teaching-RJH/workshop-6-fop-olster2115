# 1.1
sample_bay_list = ["Basalt", "Silica", "Iron", "Dust"]   
# 1.12
print(sample_bay_list[0])
# 1.13
last_item = sample_bay_list[-1]

print(last_item)
# 1.14
all_sample_bay = len(sample_bay_list)

print(all_sample_bay)
# 1.21-1.22
for sample in sample_bay_list :
    print(sample)
    print("transmitting data: [sample name]")
# 1.31
new_findings = [" "," "," "," "]
#1.32
for new_findings in range (3):
    new_findings = input(f"enter name of new material {new_findings + 1}:")
    new_findings.append("input")
    print(f"entered:{new_findings} ")
