import matplotlib.pyplot as plt

def open_file(file_name):
    x_counter = 0
    x = []
    y = []

    with open(file_name) as file:

        for row in file:
            row = row.split()
            x_counter += 1
            if x_counter == 1:

                xlabel = row[0]
                ylabel = row[1]


            else:
                x.append(float(row[0]))
                y.append(float(row[1]))

        return x, y, xlabel, ylabel


x, y, xlabel, ylabel = open_file('Jacob Kahn - time_and_temp.txt')

                 #############
################## PROBLEM 1 ##################
                 #############
## PROBLEM 1a

def plot_data(x, y, title, xlabel, ylabel, plot_code):
    xmin = min(x)
    xmax = max(x)

    ymin = min(y)
    ymax = max(y)

    plt.title(f'{title}')

    plt.xlabel = xlabel
    plt.ylabel = ylabel

    plt.plot(x, y, plot_code)

    plt.axis([xmin, xmax, ymin, ymax])

    plt.show()


plot_data(x, y, 'KOBIS GRAPH', xlabel, ylabel, '--.r')