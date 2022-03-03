from pydantic import BaseModel, HttpUrl


class Student(BaseModel):

    id: str
    nickname: str
    last_name: str
    first_name: str
    score: float
    url: HttpUrl

    
jerry = Student(**{'id': 1, 'nickname': 'jerry', 'last_name': 'Geofrey', 'first_name': 'jerry', 'score': 66.66, 'url': 'http://baidu.com'})
print(jerry)
tony = Student(
    id=2, nickname='tony', last_name='jia', first_name='tony', score=88.88,
    url='http://baidu.com'
)
print(tony)

