"""
Генератор тестовых данных для задания 6: Анализ фильмов 
Создает три файла:
1. films.csv - данные об films
2. view.xlsx - данные о view
3. producer.json - данные о producer
"""
import pandas as pd
import numpy as np
import json
import os
import random


np.random.seed(42)
random.seed(42)


film_titles = ["F1", "God father", "Lost City", "avengers", "Bullet train",
               "X-man", "Vanhelsing", "Interstellar", "Parasites", "Obsession","tik-tak boom"]

countries = ["USA", "UK", "France", "Germany", "Japan", "China", "Russia", "India","Argentina",
             "Portugal","Norway","Finland","Kazahstan","Spain"]

director_names = ["Steven Spielberg", "Christopher Nolan", "Quentin Tarantino", "James Cameron",""
                  "Martin Scorsese", "Alfred Hitchcock", "Ridley Scott", "Peter Jackson"]

#  films.csv 
def generate_films_data(num_films=1000):

    films_data = []
    
    for i in range(1, num_films+1):
        film_id = f"film{i:05d}"
        title = random.choice(film_titles) + f" {random.randint(1,1000)}"
        director_id = f"director{random.randint(1, len(director_names)):03d}"
        
        films_data.append({
            "film_id": film_id,
            "title": title,
            "director_id": director_id
        })
    
    df_films = pd.DataFrame(films_data)
    df_films.to_csv('data/films.csv', index=False, encoding='utf-8')
    print("✓ Файл films.csv создан")
    return films_data

#  view.xlsx 
def generate_views_data(films_data):

    views_data = []
    
    for film in films_data:
        film_id = film['film_id']
        country = random.choice(countries)
        views = random.randint(1000, 1000000)
        
        views_data.append({
            "film_id": film_id,
            "country": country,
            "views": views
        })
    
    df_views = pd.DataFrame(views_data)
    df_views.to_excel('data/view.xlsx', index=False)
    print("✓ Файл view.xlsx создан")
    return views_data

#  producer.json 
def generate_producers_data():
    
    producers_data = []
    
    for i, name in enumerate(director_names, start=1):
        producers_data.append({
            "director_id": f"director{i:03d}",
            "director_name": name
        })
    
    with open('data/producer.json', 'w', encoding='utf-8') as f:
        json.dump(producers_data, f, ensure_ascii=False, indent=2)
    
    print("✓ Файл producer.json создан")
    return producers_data


def main():
    print("Генерация тестовых данных для фильмов...")
    print("=" * 50)
    
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✓ Создана папка 'data'")
    
    films_data = generate_films_data()
    generate_views_data(films_data)
    generate_producers_data()
    
    print("=" * 50)
    print(f"Сгенерировано:")
    print(f"- films: {len(films_data)}")
    print("\nВсе файлы сохранены в папке 'data/'")

if __name__ == "__main__":
    main()