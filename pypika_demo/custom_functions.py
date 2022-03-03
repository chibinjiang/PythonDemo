from pypika import Table, CustomFunction, Parameter
from pypika.queries import QueryBuilder
from pypika.terms import Star, Field

DATE_FORMAT = CustomFunction('DATE_FORMAT', ['date', 'format_str'])
DATE_DIFF = CustomFunction('DATEDIFF', ['start_date', 'end_date'])
DATE_SUB = CustomFunction('DATE_SUB', ['start_date', 'interval'])

star = Star()


def format_where_clause(t: Table, query: QueryBuilder, filters: dict):
    values = list()
    for _key, _value in filters.items():
        f_field: Field = getattr(t, _key)
        if isinstance(_value, (int, float)):
            query = query.where(f_field.eq(Parameter('%s')))
        elif isinstance(_value, str):
            query = query.where(f_field.like(Parameter('%s')))
        elif isinstance(_value, (list, tuple)):
            query = query.where(f_field.isin(Parameter('%s')))
        else:
            raise Exception(f"Unknown Value Type: {type(_value)} for {_value}")
        values.append(_value)
    return query, values

