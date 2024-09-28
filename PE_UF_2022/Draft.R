library(sp)
library(sf)
library(leaflet)
library(tidyverse)

setwd('C:\\Users\\napol\\OneDrive\\UFRPE\\2023.1\\Renata\\PE_UF_2022')




df = tribble(
  ~municipio, ~apicultores, ~mulheres, ~producao,~lng, ~lat,
  'Bonito', 50, 30, '10 mil litros', -35.7265, -8.47038,
  'Barreiros', 100, 60, '10 mil litros', -35.1901, -8.80765,
  'Serra Talhada', 50, 30, '10 mil litros', -38.2929, -7.98526,
)


PE=read_sf('PE_UF_2022.shp')

leaflet()  %>% 
  addTiles() %>% 
  setView(lng =  -38.2929, lat=-7.98526, zoom=7) %>% 
  addPolygons(data=PE, weight=2, col = '#ffb825') %>% 
  addMarkers(
    data = df,
    lng = df$lng,
    lat = df$lat,
    # create custom labels
    label = paste(
      "Municício: ", df$municipio, "<br>",
      "Apicultores: ",  df$apicultores, "<br>",
      "Mulheres: ",  df$mulheres, "<br>",
      "Produção anual: ",  df$producao, "<br>"
  ) %>%
    lapply(htmltools::HTML)
  )
  
  
