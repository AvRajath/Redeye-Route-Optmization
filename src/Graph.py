import googlemaps
import pandas as pd
from helper import constants

class RouteGraph:
    def __init__(self, inputPath): 
        self.df = pd.read_excel(inputPath, index_col=None, header=None)
        self.adjacency_matrix = []
        self.gmaps = googlemaps.Client(key=constants.Constants.GOOGLEAPIKEY.value)
        #if_condition_here
        return self.form_adjacency_matrix_time()

    def form_adjacency_matrix_time(self):
        for index, row in self.df.iterrows():
            adj_mat_time = []
            for i in range(len(row)):
                temp_sub_mat_time = []
                for j in range(len(row)):
                    if (i == j):
                        temp_sub_mat_time.append(0)
                    else:
                        my_dist = self.gmaps.distance_matrix(row[i], row[j])['rows'][0]['elements'][0]
                        temp_sub_mat_time.append(my_dist['duration']['value'])
                adj_mat_time.append(temp_sub_mat_time)
            self.adjacency_matrix.append(adj_mat_time)

    def form_adjacency_matrix_distance(self):
        for index, row in self.df.iterrows():
            adj_mat_dist = []
            for i in range(len(row)):
                temp_sub_mat_dist = []
                for j in range(len(row)):
                    if (i == j):
                        temp_sub_mat_dist.append(0)
                    else:
                        my_dist = self.gmaps.distance_matrix(row[i], row[j])['rows'][0]['elements'][0]
                        temp_sub_mat_dist.append(my_dist['distance']['value'])
                adj_mat_dist.append(temp_sub_mat_dist)
            self.adjacency_matrix.append(adj_mat_dist)
