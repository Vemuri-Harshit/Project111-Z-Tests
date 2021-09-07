import plotly.figure_factory as ff;
import plotly.graph_objects as go;
import pandas as pd;
import csv;
import random;
import statistics;

df = pd.read_csv('medium_data.csv');
data = df['reading_time'].to_list();

mean = statistics.mean(data);
stdev = statistics.stdev(data);

print(mean, stdev);

def random_mean_sets(counter):
    data_set = [];
    for i in range(0, counter):
        index = random.randint(0, len(data) - 1);
        value = data[index];
        data_set.append(value);

    mean = statistics.mean(data_set);
    return mean;

mean_list = [];
for i in range(0, 1000):
    mean_set = random_mean_sets(100);
    mean_list.append(mean_set);
         
complete_stdev = statistics.stdev(mean_list);
complete_mean = statistics.mean(mean_list);

print(complete_stdev, complete_mean);

first_std_deviation_start, first_std_deviation_end = mean-complete_stdev, mean+complete_stdev
second_std_deviation_start, second_std_deviation_end = mean-(2*complete_stdev), mean+(2*complete_stdev)
third_std_deviation_start, third_std_deviation_end = mean-(3*complete_stdev), mean+(3*complete_stdev)

fig = ff.create_distplot([mean_list], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))

first_method_df = pd.read_csv('medium_data.csv');
first_method_data = first_method_df['claps'].to_list();

first_method_mean = statistics.mean(first_method_data);
first_method_stdev = statistics.stdev(first_method_data);

fig.add_trace(go.Scatter(x=[first_method_mean, first_method_mean],y=[0, 0.17], mode="lines", name="FIRST METHOD MEAN"));



fig.show()
