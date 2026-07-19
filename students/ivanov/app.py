   import streamlit as st
   from sklearn.ensemble import RandomForestRegressor
   import plotly.graph_objects as go
   
   # Обучаем модель
   model = RandomForestRegressor()
   
   # Строим график
   fig = go.Figure()
   fig.add_trace(go.Scatter(x=[1,2,3], y=[1,2,3]))
