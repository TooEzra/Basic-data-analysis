# Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]
print("Ward 4A:", ward_4a)  # Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James']

# New admission
ward_4a.append("Bed4: Aisha")
ward_4a.insert(2, "Bed7: Zain")  # Insert at specific position
print("Ward 4A:", ward_4a)
# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James', 'Bed4: Aisha']
#remove a patient
ward_4a.remove("Bed7: Zain")  # Remove by value
print("Ward 4A:", ward_4a)

# Discharge patient
discharged = ward_4a.pop(1)
print(f"Discharged: {discharged} → Remaining: {ward_4a}")
# Output: Discharged: Bed2: Fatima → Remaining: ['Bed1: Robert', 'Bed3: James', 'Bed4: Aisha']

discharged = ward_4a.pop()  # Discharge last patient
print(f"Discharged: {discharged} → Remaining: {ward_4a}")
# Output: Discharged: Bed4: Aisha → Remaining: ['Bed1: Robert

discharged = ward_4a.pop(1)  # Discharge first patient
print(f"Discharged: {discharged} → Remaining: {ward_4a}")
# Output: Discharged: Bed3: James → Remaining: ['Bed1: Robert']

discharged = ward_4a.pop(0)  # Discharge first patient
print(f"Discharged: {discharged} → Remaining: {ward_4a}")
# Output: Discharged: Bed1: Robert → Remaining: []
# Now the ward is empty

print("Ward_4A")
