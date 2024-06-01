#!/usr/bin/python3
"""api requests"""
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        postsData = [{"id": post["id"], "title": post["title"],
                      "body": post["body"]} for post in posts]

        with open("posts.csv", 'w') as csvFile:
            keys = ["id", "title", "body"]
            dicti = csv.DictWriter(csvFile, fieldnames=keys)

            dicti.writeheader()
            for post in postsData:
                dicti.writerow(post)
