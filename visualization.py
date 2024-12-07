import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_hexagon(ax, x, y, size, color, label):
  
    angle = 60 
    hexagon = patches.RegularPolygon((x, y), numVertices=6, radius=size, 
                                      orientation=0, color=color, ec='black')
    ax.add_patch(hexagon)
    ax.text(x, y, label, ha='center', va='center', fontsize=8, color='white')


def visualize_seq(sequence, nucleotide_colors, hexagon_size=0.5, nucleotides_per_row=20):
   
    fig, ax = plt.subplots(figsize=(15, 2))  

    x_spacing = 1.5 * hexagon_size
    y_position = 0


    for i, nucleotide in enumerate(sequence):
        x_position = i * x_spacing
        color = nucleotide_colors.get(nucleotide, "gray")
        draw_hexagon(ax, x_position, y_position, hexagon_size, color, nucleotide)

    
    total_width = nucleotides_per_row * x_spacing
    ax.set_xlim(-1, total_width + 1)
    ax.set_ylim(-1, 1)

    
    ax.axis('off')


    fig.tight_layout()
    plt.show()
