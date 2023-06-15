import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

locations = {
    'NADRA Mega Center': [24.84259861162998, 67.07104673604293],
    'NADRA Office Korangi': [24.83169375896178, 67.16237058972585],
    'NADRA Office Saddar': [24.858555173919363, 67.02361519504058],
    'NADRA Office Landhi': [24.83941495558677, 67.22467030400203],
    'NADRA Office North Nazimabad': [24.946468679478286, 67.05136162387892],
    'NADRA Office Malir': [24.882811045752813, 67.14026578200338],
    'NADRA Office Liaquatabad': [24.910043900272203, 67.03820763802689],
    'NADRA Office Clifton': [24.829131320227233, 67.03415796261255],
    'NADRA Office Gulistan-e-Jauhar': [24.93755284679499, 67.16936644043551],
    'NADRA Office Gulshan-e-Iqbal': [24.918201740488435, 67.09774957368647],
    'NADRA Office Shah Faisal Colony': [24.885248976512464, 67.14668822047112],
    'NADRA Office DHA': [24.837600809619797, 67.06912868880077],
    'NADRA Office Gulshan-e-Maymar': [25.03189420932269, 67.13621834744535],
    'NADRA Office Malir Cantt': [24.904126971966065, 67.19687810850012],
    'NADRA Office Gulshan-e-Hadeed': [24.865769168001904, 67.35188512387606],
    'NADRA Office Lyari': [24.862555378795317, 66.99921096870268],
    'NADRA Office Baldia Town': [24.992612314892007, 66.99424709968189],
    'NADRA Office Orangi Town': [24.942151854916947, 66.9982753315495],
    'NADRA Office Defence View Society': [24.84388970787065, 67.05936045003564],
    'NADRA Office Surjani Town': [25.01894931061408, 67.0641981369601],
    'NADRA Office Gulistan-e-Johar': [24.91788823269317, 67.14986250972201],
    'NADRA Office Bahadurabad': [24.884084355475657, 67.08533981462186],
    'NADRA Office Malir City': [24.872177192700356, 67.19743721406957]
}   

df = pd.DataFrame.from_dict(locations, orient='index', columns=['Latitude', 'Longitude'])

st.title("NADRA Offices")

search_term = st.text_input("Search NADRA office:", '')

filtered_df = df[df.index.str.contains(search_term, case=False)]

if not filtered_df.empty:

    m = folium.Map(location=[24.8607, 67.0011], zoom_start=11)

    for index, row in filtered_df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=index,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

    folium_static(m)
else:
    st.write("No matching locations found.")
