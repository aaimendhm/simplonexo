import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte * prix', names='produit', title='chiffre d affaire par produits')

figure.write_html('chiffre-d-affaire-par-produits.html')

print('chiffres-d-affaire-par-produits.html généré avec succès !')
