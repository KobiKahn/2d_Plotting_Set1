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

def open_special_file(filename):
    x = 0
    time_data = []
    temp_data = []
    pressure_data = []
    volume_data = []
    with open(filename) as file:

        for row in file:
            row = row.split()
            x += 1
            if x == 1:
                time_label = row[0]
                temp_label = row[1]
                pressure_label = row[2]
                volume_label = row[3]

            else:
                time_data.append(float(row[0]))
                temp_data.append(float(row[1]))
                pressure_data.append(float(row[2]))
                volume_data.append(float(row[3]))
    return(time_label, time_data, temp_label, temp_data, pressure_label, pressure_data, volume_label, volume_data)


def draw_subplot(r, c, time_label, time_data, temp_label, temp_data, pressure_label, pressure_data, volume_label, volume_data):

    temp_avg = 0
    pressure_avg = 0
    volume_avg = 0

    x = 0

    time_min = min(time_data)
    time_max = max(time_data)

    temp_min = min(temp_data)
    temp_max = max(temp_data)

    pressure_min = min(pressure_data)
    pressure_max = max(pressure_data)

    volume_min = min(volume_data)
    volume_max = max(volume_data)

    for num in temp_data:
        x += 1
        temp_avg += int(num)

    temp_avg /= x

    x = 0

    for num in pressure_data:
        x += 1
        pressure_avg += int(num)

    pressure_avg /= x

    x = 0

    for num in volume_data:
        x += 1
        volume_avg += int(num)

    volume_avg /= x

    x = 0

    plt.subplot(r, c, 1)

    plt.plot(time_data, temp_data)
    plt.xlabel = time_label
    plt.ylabel = temp_label
    plt.axis([time_min, time_max, temp_min, temp_max])

    plt.axhline(y = temp_avg,color = 'r', linestyle = '-')

    plt.subplot(r,c,2)

    plt.plot(time_data, pressure_data)
    plt.xlabel = time_label
    plt.ylabel = pressure_label
    plt.axis([time_min, time_max, pressure_min, pressure_max])

    plt.axhline(y=pressure_avg, color='r', linestyle='-')

    plt.subplot(r, c , 3)

    plt.plot(time_data, volume_data)
    plt.xlabel = time_label
    plt.ylabel = volume_label
    plt.axis([time_min, time_max, volume_min, volume_max])

    plt.axhline(y=volume_avg, color='r', linestyle='-')

    plt.show()




time_label, time_data, temp_label, temp_data, pressure_label, pressure_data, volume_label, volume_data = open_special_file('Jacob Kahn - time_temp_pressure_volume.txt')

draw_subplot(3, 1, time_label, time_data, temp_label, temp_data, pressure_label, pressure_data, volume_label, volume_data)
