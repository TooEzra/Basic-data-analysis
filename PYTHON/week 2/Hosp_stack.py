#Medication Dispensing -Last-In-First-Out (LIFO) for efficient medicine access
# Pharmacy Medication Stack
medication_stack = []

# Stock medications (newest on top)
medication_stack.append("Antibiotics")
medication_stack.append("Painkillers")
medication_stack.append("Insulin")
medication_stack.append("Cetrizine")
medication_stack.append("Ibuprofen")

print("Pharmacy Stock:", medication_stack)
# Output: ['Antibiotics', 'Painkillers', 'Insulin']

# Dispense medications
for _ in range(3):
    dispensed = medication_stack.pop()
    print(f"Dispensed: {dispensed} → Remaining: {medication_stack}")

    
