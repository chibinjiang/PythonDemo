from tables import DemoTable
from pypika import MySQLQuery, Order
from pypika.terms import Interval
from pypika.functions import Count
from pypika.analytics import Avg, StdDev, Median
from custom_functions import DATE_FORMAT, format_where_clause, star, DATE_SUB


def test_date_format():
    print("\n\n>>>>> test_date_format()")
    stmt = MySQLQuery.from_(DemoTable) \
        .select(
            DATE_FORMAT(DemoTable.comment_time, "%Y-%m-%d").as_("date"),
            Count(star).as_('count')
        ).groupby(1) \
        .having(Count(star) > 1) \
        .orderby('count', order=Order.desc)
    print("SQL: ", stmt.get_sql())
    return stmt.get_sql()


def test_group_and_where_clause():
    print("\n\n>>>>> test_group_and_where_clause()")
    stmt = MySQLQuery.from_(DemoTable) \
        .select(
            DemoTable.country.as_('value'),
            Count(star).as_('count')
        )

    filters = {
        'name': 'Chibin Jiang',
        'age': 28,
        'country': ['CN', 'US']
    }
    stmt, values = format_where_clause(DemoTable, stmt, filters)
    print("After Add Where: ", stmt)
    print("Values: ", values)
    stmt = stmt.groupby(1).orderby('count', order=Order.desc)
    print("SQL: ", stmt.get_sql())
    return stmt.get_sql()


def test_join_query():
    """
        select t1.*, t2.* from (
          select cst_date, count(*)
          from yolobase.t_feedback
          group by 1
        ) t1 join (
          select cst_date, count(*)
          from yolobase.t_feedback
          group by 1
        ) t2 where t1.cst_date = t2.cst_date;
        -- using cst_date
    """
    print("\n\n>>>>> test_join_query()")
    t1 = MySQLQuery.from_(DemoTable) \
        .select(DemoTable.cst_date, Count("*").as_('count')) \
        .groupby(1).as_('t1')
    t2 = MySQLQuery.from_(DemoTable) \
        .select(DemoTable.cst_date, Count("*").as_('count')) \
        .groupby(1).as_('t2')
    stmt = MySQLQuery.from_(t1).join(t2) \
        .using('cst_date').select(t1.star, t2.star)
    print("SQL: ", stmt.get_sql())
    return stmt.get_sql()


def test_join_query_and_date_functions():
    """
        select t1.*, t2.* from (
          select cst_date, count(*)
          from yolobase.t_feedback
          group by 1
        ) t1 join (
          select cst_date, count(*)
          from yolobase.t_feedback
          group by 1
        ) t2 where t1.cst_date = t2.cst_date;
        -- using cst_date
    """
    print("\n\n>>>>> test_join_query_and_date_functions()")
    t1 = MySQLQuery.from_(DemoTable) \
        .select(DemoTable.cst_date, Count("*").as_('count')) \
        .groupby(1).as_('t1')
    t2 = MySQLQuery.from_(DemoTable)\
        .select(DemoTable.cst_date, Count("*").as_('count'))\
        .groupby(1).as_('t2')
    stmt = MySQLQuery.from_(t1).join(t2) \
        .on(DATE_SUB(t1.cst_date, Interval(days=1)).eq(t2.cst_date)) \
        .select(t1.star, t2.star)
    # 使用INTERVAL instead of 'INTERVAL 1 DAY'
    print("SQL: ", stmt.get_sql())
    return stmt.get_sql()


def test_math_functions():
    print("\n\n>>>>> test_math_functions()")
    median_income = Median(DemoTable.annual_income) \
        .over(DemoTable.customer_state).as_('MEDIAN')
    avg_income = Avg(DemoTable.annual_income) \
        .over(DemoTable.customer_state).as_('AVG')
    stddev_income = StdDev(DemoTable.annual_income) \
        .over(DemoTable.customer_state).as_('STDDEV')

    stmt = MySQLQuery.from_(DemoTable) \
        .select(median_income, avg_income, stddev_income) \
        .where(DemoTable.customer_state.isin(['DC', 'WI'])) \
        .orderby(DemoTable.customer_state)
    print("SQL: ", stmt.get_sql())
    return stmt.get_sql()


if __name__ == "__main__":
    test_date_format()
    test_group_and_where_clause()
    test_join_query_and_date_functions()
    test_math_functions()
