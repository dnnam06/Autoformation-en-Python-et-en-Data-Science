import pandas as pd

df = pd.read_csv("table_csv/table_netflix.csv")

# print all the movies
movie = df[df["type"] == "Movie"]
total_movies = movie["type"].count()

# print and count all the american movies
american_movies = df[(df["type"] == "Movie") & (df["country"].str.contains("United States", na=False))]
total_ame_movies = american_movies["type"].count()

# add a column called "date_formatted" to reformat the dates given
df["date_formatted"] = pd.to_datetime(df["date_added"], errors="coerce")
date_210921 = df[df["date_formatted"] == "2021-09-21"]
# print(date_210921["type"].count())
month_09 = df[(df["date_formatted"].dt.month == 9.0)]
# print(month_09["type"].count())
day_01_10_m09 = df[(df["date_formatted"].dt.month == 9.0) & (df["date_formatted"].dt.day >= 1.0) & (df["date_formatted"].dt.day <= 10.0)]
# print(day_01_10_m09["type"].count())


filtered = df[(df["date_formatted"].dt.month == 9.0) & (df["type"] == "Movie") & (df["country"].str.contains("United States", na=False)) & (df["date_formatted"].dt.day >= 1.0) & (df["date_formatted"].dt.day <= 10.0)]
grouped = filtered.groupby(filtered["date_formatted"].dt.year)
# print(grouped.count())


# HW : find short movies (time under 70 minutes) for adults
int_duration = pd.to_numeric(df["duration"].str.replace(" min",""), errors="coerce")
short_movies_for_adults = df[(df["type"] == "Movie") & (df["rating"].str.contains("TV-MA", na=False)) & (int_duration <= 70)]
# print(short_movies_for_adults.count())

# find the actor / actress who has acted in the most movies / in most short movies for under-13 teenagers
actors = df[df["type"] == "Movie"]["cast"].dropna().str.split(", ").explode()
top_actor = actors.value_counts().head(1)
top_actor_name = top_actor.idxmax()
top_actor_count = top_actor.max()
print(top_actor_name, top_actor_count)

actors_for_U13 = df[(df["type"] == "Movie") & (df["rating"].str.contains("PG-13", na=False))]["cast"].dropna().str.split(', ').explode()
top_actor_for_U13 = actors_for_U13.value_counts().head(1)
# print(top_actor_for_U13.idxmax(), top_actor_for_U13.max())
