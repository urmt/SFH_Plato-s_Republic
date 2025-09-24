import matplotlib.pyplot as plt
import numpy as np
from IPython import display

# Setup 10x10 grid
grid = np.zeros((10, 10))

# ROYGBIV colormap (HSV, 0=red to 270=violet)
cmap = plt.get_cmap('hsv')

# Create a single figure with 2x5 subplot grid for 10 frames
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
axes = axes.flatten()  # Flatten for easy iteration

# Simulate 10 frames
for frame in range(10):
    # Update loop
    grid += 0.1 * (np.random.rand(10, 10) - 0.5)
    grid = np.clip(grid, 0, 1)
    
    # Plot on the current subplot
    im = axes[frame].imshow(grid, cmap=cmap, vmin=0, vmax=1)
    axes[frame].set_title(f'Frame {frame}: Avg = {np.mean(grid):.2f}')
    axes[frame].axis('off')

# Adjust layout and display
plt.tight_layout()
display.display(plt.gcf())  # Display all frames at once

# Explanation for SFH Simulation
"""
## Understanding the SFH Qualic Simulation

This script simulates a 10x10 grid representing the Sentient Field Hypothesis (SFH) from *The Sentient Republic*. Each of the 100 cells models a unit of qualic coherence, measuring the alignment of the sentient field's projections (linked to consciousness).

### What the Colors Mean
Coherence ranges from 0.0 to 1.0, mapped to ROYGBIV using HSV:
- **Red (0.0)**: Minimal coherence (chaos).
- **Orange-Yellow-Green (0.3-0.6)**: Moderate coherence (balance).
- **Blue-Indigo-Violet (1.0)**: High coherence (harmony).
Cells start at 0 (red) and fluctuate, stabilizing around 0.5 (green-yellow).

### Why Changes Are Subtle
Slow, random adjustments mimic natural drift; all 10 frames are shown simultaneously.

### Real-World Context
In Kallifield, this represents Weavers' consciousness—violet for attunement.

### Enhancement Ideas
Add interactions or animate frames with a library like p5.js.
"""