# 1D Uniform Flow Calculation
#     in Compound Channel
#     Using Newton Method

# Calculation of Water Level
# Type 01 with input data inside code

# Problem Statement
# Compound Rectangular Channel
# with same width of channel and floodplain
# Channel water depth = Floodplain water depth + 2
# Following are the channel data

# Input
Q = 80          # Discharge(cu m per sec)
W = 10          # River and Floodplain Width
S = 1/500       # Channel Slope
n_f = 0.04      # Floodplain Roughness Co-efficient
n_c = 0.03      # Channel Roughness Co-efficient
error = 0.001   # Acceptable error

# Calculate Floodplain Water Depth

# Calculate Constant
C_f = W * S**0.5 / n_f
C_c = W * S**0.5 / n_c

# Assuming Initial Condition
H_f = 2

# Number of Iterations
N = 100

print(f"{'Initial Value':<15}"                                          # Result Header
      f"{'New Value':<15}"
      f"{'Error':<15}"
      f"{'Estimated Discharge':<20}")

# Start Iterations
for i in range(N):
    F = C_f * H_f**(5/3) + C_c * (H_f + 2)**(5/3) -Q                    # Function
    DF = 5/3 * C_f * H_f**(5/3-1) + 5/3 * C_c * (H_f + 2)**(5/3-1)      # Derivative of Function

    H_f_new = H_f - (F/DF)                                              # Calculating New Initial Condition

    q = C_f * H_f ** (5 / 3) + C_c * (H_f + 2) ** (5 / 3)               # Check Discharge

    e = abs(H_f - H_f_new)                                              # Calculating Error

    print(f"{round(H_f, 4):<15}"                                        # Print Calculation Table
          f"{round(H_f_new, 4):<15}"
          f"{round(e, 4):<15}"
          f"{round(q, 4):<20}")

    H_f = H_f_new                                                       # Overwriting Initial Condition

    if e < error:                                                       # Stop Iteration with allowable error
        break

print("  ")
print("Water Level in Floodplain is: ",round(H_f,4))                    # Print Result


# End
