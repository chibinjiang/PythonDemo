from pydantic import BaseModel, ValidationError


class Student(BaseModel):
    first_name: str
    last_name: str

    class Config:
        max_anystr_length = 5
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


tony = Student(first_name='tony', last_name='wula lawu')
#try:
#    Model(v='x' * 10)
#except ValidationError as e:
#    print(e)

