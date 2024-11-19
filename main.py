import numpy as np
import matplotlib as mpl
import matplotlib.animation
import matplotlib.pyplot as plt
import skimage


no_frames = 64

no_wings_1 = 3
rpm_1 = 1000

no_wings_2 = 5
rpm_2 = 8000


def propeller_func(x, m, no_w, rpm_):
    if not(0 <= rpm_ <= 10000):  # Sprawdzamy czy RPM jest w danym zakresie
        print('RPM out of range!')
    else:
        rpm_ = 10 - rpm_ / 1000

    r = np.sin(no_w * x + m * np.pi / rpm_)

    return r


def create_subplot(ax, no_w, rpm_, frame):
    ax.clear()  # Czyścimy wykres / odświeżamy
    m = frame - no_frames / 2  # Ustawiamy m tak, aby było w zakresie od -M/2 do M/2, gdzie M = 'frames'
    x = np.linspace(0, 2 * np.pi, 500)  # Tworzymy ciąg równomiernie rozstawionych pkt na OX (1000 to gęstość)
    r = propeller_func(x, m, no_w, rpm_)
    ax.plot(x, r)
    ax.set_rmax(1.0)
    ax.set_yticklabels([])
    ax.set_title(f'Frame: {frame}; Wings: {no_w}; RPM: {rpm_}')
    ax.grid(True)

    return ax


fig, plots = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
fig.subplots_adjust(wspace=0.5)


def draw(frame):
    create_subplot(plots[0], no_wings_1, rpm_1, frame)
    create_subplot(plots[1], no_wings_2, rpm_2, frame)

    return plots


anim = mpl.animation.FuncAnimation(fig, draw, frames=no_frames, interval=100)

plt.show()


# Sensor part

def pol_to_cart(theta, r):
    x = r * np.cos(theta)
    y = r * np.sin(theta)

