from matplotlib import pyplot as plt


def matrix_show(matrix):
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.axis('off')
    tb = ax.table(cellText=matrix, loc='center', cellLoc='center')
    tb.auto_set_font_size(False)
    tb.set_fontsize(8)
    plt.show()