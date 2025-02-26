# Soil Survey
The data in `soil_data.csv` is produced from Arizona soil data taken from SSURGO [here](https://websoilsurvey.nrcs.usda.gov/app/WebSoilSurvey.aspx). The csv is produced from the associated notebook.


# Notes
Each area has comes with tabular and spatial information. 


## Map Unit
The map units delineated on the detailed soil maps in a soil survey represent the soils or miscellaneous areas in the survey area. A map unit delineation on a soil map represents an area dominated by one or more major kinds of soil or miscellaneous areas. A map unit is identified and named according to the taxonomic classification of the dominant soils.

Soils that have profiles that are almost alike make up a soil series. All the soils of a series have major horizons that are similar in composition, thickness, and arrangement. Soils of a given series can differ in texture of the surface layer, slope, stoniness, salinity, degree of erosion, and other characteristics that affect their use. On the basis of such differences, a soil series is divided into soil phases. Most of the areas shown on the detailed soil maps are phases of soil series. The name of a soil phase commonly indicates a feature that affects use or management. For example, Alpha silt loam, 0 to 2 percent slopes, is a phase of the Alpha series.

Some map units are made up of two or more major soils or miscellaneous areas. These map units are complexes, associations, or undifferentiated groups.

A complex consists of two or more soils or miscellaneous areas in such an intricate pattern or in such small areas that they cannot be shown separately on the maps. The pattern and proportion of the soils or miscellaneous areas are somewhat similar in all areas. Alpha-Beta complex, 0 to 6 percent slopes, is an example.

An association is made up of two or more geographically associated soils or miscellaneous areas that are shown as one unit on the maps. Because of present or anticipated uses of the map units in the survey area, it was not considered practical or necessary to map the soils or miscellaneous areas separately. The pattern and relative proportion of the soils or miscellaneous areas are somewhat similar. Alpha-Beta association, 0 to 2 percent slopes, is an example.

An undifferentiated group is made up of two or more soils or miscellaneous areas that could be mapped individually but are mapped as one unit because similar interpretations can be made for use and management. The pattern and proportion of the soils or miscellaneous areas in a mapped area are not uniform. An area can be made up of only one of the major soils or miscellaneous areas, or it can be made up of all of them. Alpha and Beta soils, 0 to 2 percent slopes, is an example.

Some surveys include miscellaneous areas. Such areas have little or no soil material and support little or no vegetation. Rock outcrop is an example.


## Key Info

### Map Unit
A map unit delineation on a soil map represents an area dominated by one or more major kinds of soil or miscellaneous areas. A map unit does not need to be single enclosed polygon. It could be a collection of polygons with same type.

A collection of soil areas, defined and named, delineated of the map and are uniquely identified. These are usually delineated based on soil boundaries or other patterns in the soil. Identified the pattern of each component. 

There are different kind of map units:
- consociation: dominated by one component
- complexes and associations: two or more dissimilar components that occur in a regularly repeating patttern
- major components of a complex cannnot be mapped separately
- undifferentiated group: two or more components that are not each present 

Map units have a name which is generally based on the type of soil and the phases. The soil is the first bit, the phases are the land forms e.g. slope.

### Soil Types
Different soil types are assigned a series name to communicate easily.


### Components
A component is basically one set / composition of soils. It is made up of different series names (soil types) and the percentages within the map unit. It's essentially a collection of soils
 
A map unit can be made of up of different amounts of a component and also each component can have different layers as well as well.


- MUSYM: The symbol used to uniquely identify the soil mapunit in the soil survey.
- MUACRES: The number of acres of a particular mapunit.
- FARMLNDCL: Identification of map units as prime farmland, farmland of statewide importance, or farmland of local importance.
- MUKEY: Unique ID for a Map Unit


### Horizons
These are the different layers in a soil or component. They are typically classified:

These are the master horizons. They have unique chemical, physical and biological properties

- O: plant / organic matter
- A: mineral, high prop of organic matter
- E: light, maximum zone of leeching
- B: Maximum zone of accumulation
- C: 
- R: Bedrock

Then there are subscripts like 'Ap', where the 'p' is the subscript.



## Spatial Data
The spatial information can be loaded in python using [geopandas](https://geopandas.org/en/stable/index.html). There are different spatial data files. The file name prefixes are explained below:

- soilsa_a: soil survey area boundary polygon(s)
- soilmu_a: map unit boundary polygons
- soilmu_l: line map units
- soilmu_p: point map units
- soilsf_l: line spot features
- soilsf_p: point spot features
- soilsf_t: spot feature descriptions

There are also different file types. 

There are 3 key files associated with any and all shapefiles:
- .shp: the file that contains the geometry for all features.
- .shx: the file that indexes the geometry.
- .dbf: the file that stores feature attributes in a tabular format.
- .prj: the file that contains information on projection format including the coordinate system and projection information. It is a plain text file describing the projection using well-known text (WKT) format.