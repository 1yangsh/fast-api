# https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless
# (FastAPI로 Serverless 구축하기)
from typing import Optional
from fastapi import FastAPI
from mangum import Mangum
import psycopg2
from config import DB


app = FastAPI(
    title='Serverless with FastAPI',
    description='나의 첫번째 FastAPI'
)

# class DB_connect():
#     def __init__(self):g
#         self.conn = psycopg2.connect(**config)
#         self.cursor = self.conn.cursor()

@app.get("/")
def read_root():
    return "Hello, world!"

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# @app.get("/topic")
# def get():
#     sql = "SELECT * FROM topic"
#
#     with conn.cursor() as cursor:
#         cursor.execute(sql)
#         result_set = cursor.fetchall()
#
#         row_headers = [x[0] for x in cursor.description]
#
#         json_data = []
#         for result in result_set:
#             json_data.append(dict(zip(row_headers, result)))
#
#         return json_data
#
#
# @app.get("/topic/{tid}")
# def get(tid: int):
#
#
#     sql = f"select * from topic where tid={tid}"
#
#     cursor.execute(sql)
#     result_set = cursor.fetchall()
#
#     row_headers = [x[0] for x in cursor.description]
#
#     json_data = []
#
#     for result in result_set:
#         json_data.append(dict(zip(row_headers, result)))
#
#     return json_data
#
# @app.get('/profile')
# def get():
#     conn = psycopg2.connect(**config)
#     cursor = conn.cursor()
#
#     sql = "select * from profile"
#
#     cursor.execute(sql)
#     result_set = cursor.fetchall()
#
#     row_headers = [x[0] for x in cursor.description]
#
#     json_data = []
#
#     for result in result_set:
#         json_data.append(dict(zip(row_headers, result)))
#
#     return json_data


# class Topic(DB_connect):
#     def get(self):
#         sql = "select * from topic"
#         self.cursor.execute(sql)
#         result_set = self.cursor.fetchall()
#         row_headers = [x[0] for x in self.cursor.description]
#         print(self.cursor.description)
#
#         json_data = []
#         for result in result_set:
#             json_data.append(dict(zip(row_headers, result)))
#
#         return jsonify(json_data)



handler = Mangum(app)