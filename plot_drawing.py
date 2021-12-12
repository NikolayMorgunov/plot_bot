import matplotlib.pyplot as plt
import csv


def comma(s):
    for i in range(len(s)):
        if s[i] == ',':
            s = s[:i] + '.' + s[i + 1:]
    return s


def plot_drawing(ax_x_name, ax_y_name, ax_x_scale, ax_y_scale, scatter, legend):
    fig, ax = plt.subplots()
    ax.set_xlabel(ax_x_name)
    ax.set_ylabel(ax_y_name)
    ax.set_xscale(ax_x_scale)
    ax.set_yscale(ax_y_scale)

    with open('file.csv') as file:
        reader = csv.reader(file, delimiter=',', quotechar='\"')
        x = []
        y = []
        n = 0
        for i in reader:
            if i[0]:
                x.append(float(comma(i[0])))
                y.append(float(comma(i[1])))
            else:
                if scatter:
                    ax.scatter(x, y)
                else:
                    ax.plot(x, y)
                x = []
                y = []
                n += 1

        if x:
            n += 1
            if scatter:
                ax.scatter(x, y)
            else:
                ax.plot(x, y)

        if legend:
            legend_official = [(i + 1) for i in range(n)]
            for i in enumerate(legend):
                if i[0] == n:
                    break
                legend_official[i[0]] = i[1]
            ax.legend(legend_official)

        ax.grid(which='major',
                color='k',
                linewidth=2)
        ax.grid(which='minor',
                color='k',
                linestyle=':')
        ax.minorticks_on()
        plt.savefig('plot.png')
        return 'plot drawn'


if __name__ == '__main__':
    plot_drawing('x', 'y', 'linear', 'linear', True, ['Квадрат', 'Корень'])
