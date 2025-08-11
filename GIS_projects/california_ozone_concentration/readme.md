# ★ California Ozone Concentration & Socioeconomic Impact Analysis ★

## ★ Problem ★
Ground-level ozone, while beneficial in the upper atmosphere, poses significant health risks when present in the air we breathe.  
Understanding **what causes ozone buildup** and whether it **disproportionately affects certain populations** is critical for public health planning in California.  
Key challenges include:
- Ozone levels vary with **geographic and environmental factors** like elevation.
- Potential inequities in exposure based on **socioeconomic status**.
- Complex spatial relationships between monitoring stations, elevation data, and population demographics.

---

## ★ Purpose ★
This project aimed to:
- Investigate the **relationship between ozone concentration and elevation** across California.
- Assess whether **ozone exposure correlates with household income** levels.
- Create a comprehensive **map-based visualization** combining ozone measurements, spatial interpolation, and socioeconomic data.

---

## ★ Solution ★
Using **ArcGIS Pro** and multi-source environmental and census datasets, I developed a geospatial workflow to:
1. **Integrate** ozone monitoring data with station locations.
2. **Extract** elevation values for each air quality monitoring station.
3. **Interpolate** ozone readings into a continuous surface.
4. **Aggregate** ozone concentrations to dissolved county boundaries for visualization.
5. **Analyze** statistical relationships between:
   - Ozone vs. Elevation
   - Household Income vs. Ozone

---

## ★ Workflow ★
1. **Data Preparation**
   - Imported:
     - Air quality stations (point data)
     - Ozone averages (tabular data, 2010–2011)
     - Census tracts with household income
     - 30m Digital Elevation Model (DEM)
   - Joined ozone data to station locations (matching `site_id`).

2. **Elevation & Ozone Analysis**
   - Extracted elevation values from DEM to stations.
   - Created scatter plot: **Ozone (Y) vs. Elevation (X)** with trendline.

3. **Income & Ozone Analysis**
   - Interpolated ozone surface from station data (TIN → Raster, 30m cell size).
   - Used **Zonal Statistics as Table** to average ozone values per census tract.
   - Created scatter plot: **Household Income (Y) vs. Ozone (X)**.

4. **Mapping & Visualization**
   - Dissolved census tracts to approximate counties using `block_id`.
   - Symbolized counties by ozone concentration (Equal Interval, 6 classes).
   - Overlaid station locations on map.
   - Added inset map showing interpolated ozone surface.

5. **Export & Documentation**
   - Labeled axes and titled graphs clearly.
   - Exported as a **single-page PDF** with both graphs and maps.

---

## ★ Tools & Technologies ★
- **ArcGIS Pro / ArcMap** (Join, Zonal Statistics, Extract MultiValues to Points, Create TIN, TIN to Raster)
- **Projection**: NAD_1983_California_Teale_Albers
- **Data Sources**:
  - California Air Resources Board (CARB)
  - US Census Bureau (American Fact Finder)
  - US Geological Survey (USGS)

---

## ★ Results ★
- **Correlation Analysis**:
  - Identified trends between ozone concentration and elevation.
  - Evaluated potential disparities between ozone exposure and income levels.
- **Visual Outputs**:
  - County-level ozone concentration map.
  - Interpolated ozone surface raster.
  - Two scatter plots for key variable relationships.

---

## ★ Project Files ★
- 📄! [map] (Geospatial_and_environmental_analysis.pdf)  
  *(Contains primary map, interpolated surface, and both scatter plots)*

