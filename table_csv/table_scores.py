import pandas as pd

data = {
    'ID_Étudiant': ['ET001', 'ET002', 'ET003', 'ET004', 'ET005'],
    'Nom': ['An', 'Binh', 'Cuong', 'Dung', 'Em'],
    'Classe': ['Terminale A1', 'Terminale A1', 'Terminale A2', 'Terminale A2', 'Terminale A3'],
    'Matière': ['Mathématiques', 'Physique', 'Chimie', 'Littérature', 'Anglais'],
    'Note_Devoir': ['15/20', '12/20', '11/20', '18/20', '14/20'],
    'Note_Examen': ['17 points', '15 points', '12 points', '19 points', '14 points'],
    'Participation': [18, 16, 14, 20, 17],
    'Absences': [0, 2, 4, 1, 3]
}

df = pd.DataFrame(data)

# =========================
# FILTRAGE SIMPLE
# =========================

condition = df['Participation'] > 15

resultat = df.loc[condition, :]

# print(resultat)

# =========================
# PLUSIEURS CONDITIONS
# =========================

condition_combinee = (
    (df['Nom'] == 'An') &
    (df['Participation'] > 15) &
    (df['Matière'] == 'Mathématiques')
)

resultat_filtre = df.loc[condition_combinee, :]

# print(resultat_filtre)

# =========================
# RECHERCHE DANS UNE CHAÎNE
# =========================

condition = df['Matière'].str.contains('math', case=False, na=False)

resultat = df.loc[condition, :]

# print(resultat)

# =========================
# NETTOYAGE DES DONNÉES
# =========================

# Copie colonne
df['Note_Examen_Numerique'] = df['Note_Examen']

# Regex :
# supprime tout ce qui n'est PAS un chiffre
regex_pattern = r'[^0-9]'

df['Note_Examen_Numerique'] = (
    df['Note_Examen_Numerique']
    .astype(str)
    .str.replace(regex_pattern, '', regex=True)
    .astype('int64')
)

# print(df[['Nom', 'Note_Examen', 'Note_Examen_Numerique']])

# =========================
# FILTRAGE APRÈS NETTOYAGE
# =========================

condition = df['Note_Examen_Numerique'] > 15

resultat = df.loc[condition, :]

print(resultat)

# =========================
# SUPPRIMER UNE COLONNE
# =========================

df.drop(
    columns=['Note_Examen_Numerique'],
    inplace=True
)

# print(df)