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

                                                                 #############
                                                ################## PROBLEM 1 ##################
                                                                 #############

## PROBLEM 1a

def plot_data(x, y, title, xlabel, ylabel, plot_code):
    counter = 0

    x_num = 0
    y_num = 0

    for int_x in x:
        counter += 1
        x_num += int_x

    for int_y in y:
        y_num += int_y

    x_avg = (x_num / counter)
    y_avg = (y_num / counter)

    centroid = [x_avg, y_avg]
    print(centroid)

    xmin = min(x)
    xmax = max(x)

    ymin = min(y)
    ymax = max(y)

    plt.title(f'{title}')

    plt.xlabel = xlabel
    plt.ylabel = ylabel

    plt.plot(x, y, plot_code)

    plt.text(centroid[0], centroid[1], 'Data Centroid')

    # plt.hlines(xmin, xmax, centroid[1])
    # plt.vlines(ymin, ymax, centroid[0])
    ######### ASK ABOUT HOW TO DO HORIZONTAL AND VERTICAL LINES

    plt.axis([xmin, xmax, ymin, ymax])

    plt.show()


## 1b
# x, y, xlabel, ylabel = open_file('Jacob Kahn - time_and_temp.txt')
# plot_data(x, y, 'KOBI\n GRAPH', xlabel, ylabel, '--.r')

#### 2
# x, y, xlabel, ylabel = open_file('Jacob Kahn - temp_and_pressure.txt')
# plot_data(x, y, 'KOBIS GRAPH', xlabel, ylabel, 'or')

###### 3
x, y, xlabel, ylabel = open_file('Jacob Kahn - time_temp_pressure_volume.txt')


