"""
The script creates a press-fit motor connector for LEGO axle
"""

from build123d import Cylinder, Box, Rotation, Location, export_step

# Dimensions
motor_diameter = 5.0
motor_flat = 0.2
motor_depth = 8.0
press_fit_reduction = 0.1  # Reduce hole size by 0.1mm for press fit

lego_depth = 8.0
total_length = motor_depth + lego_depth + 4.0  # includes small buffer

# Create outer cylinder
outer = Cylinder(radius=6, height=total_length)

# Create motor shaft hole (5mm D-shape with press fit)
motor_hole = Box(motor_diameter - press_fit_reduction, 
                4.8 - press_fit_reduction, 
                motor_depth + 2.0).translate((0, 0, motor_depth / 2 + 1))

# Create Lego axle socket (X-shape with tighter tolerance)
lego_arm = Box(4.7, 1.9, lego_depth + 2.0)  # Slightly smaller than original
lego_cross = lego_arm + lego_arm.located(Location((0, 0, 0), (0, 0, 90)))
lego_cross = lego_cross.translate((0, 0, motor_depth + lego_depth / 2 + 1))

# Subtract motor and Lego features
connector = outer - motor_hole - lego_cross

# Export as STEP
step_path = "lego_motor_connector.step"
export_step(connector, step_path)