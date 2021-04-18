# Plasmids-Plotting

This repo contains two files. Other files such as api-key and original data have not been published.

1. Plasmidmap.py
----------------
Read data and connect with Google maps API to get latitude and longitude.

2. plotting.py
--------------
To demonstrate plotting using the follwoing libraries shapely, matplotlib, geopandas to show all the places in the world where the plasmids are being used.


Objective:

A scientist who has developed the plasmids, which are biological constructs, has shared them with other scientists and professors around the world. All details such as the name and the university of all the recepients have been recorded on a spreadsheet. The main objective of this project is to help the scientist plot on a world map all the locations the plasmids are currently being used.

Input spreadsheet sample data

plasmid name                                         recipient name               university name                date 
-------------------------------------------------------------------------------------------------------------------------
Construct 32 - NFKBRp_mKate2_...............         A****** D******              Duke University          Dec. 25, 2020
Construct 32 - NFKBRp_mKate2_...............         S****** M******              Tufts University         Dec. 25, 2020
Construct 32 - NFKBRp_mKate2_...............         M****** T******              Tufts University         Dec. 25, 2020
.
.
.
