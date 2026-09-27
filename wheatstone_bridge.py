# wheatstone_bridge.py
# Program to calculate unknown resistance using Wheatstone Bridge

print("=== Wheatstone Bridge ===")

# Input values
R1 = float(input("Enter resistance R1 (Ohm): "))
R2 = float(input("Enter resistance R2 (Ohm): "))
R3 = float(input("Enter resistance R3 (Ohm): "))

# Calculate unknown resistance R4
R4 = (R2 * R3) / R1

# Display result
print("\n--- Wheatstone Bridge Result ---")
print(f"R1 = {R1:.2f} Ohm")
print(f"R2 = {R2:.2f} Ohm")
print(f"R3 = {R3:.2f} Ohm")
print(f"Unknown Resistance R4 = {R4:.2f} Ohm")

print("\nAt balance condition:")
print("R1 / R2 = R3 / R4")
