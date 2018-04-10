
def get_query_str(func: str) -> str:
    query = """
          SELECT to_timestamp(t) AT TIME ZONE 'UTC' AS X, {0} AS Y
          FROM generate_series
            ( EXTRACT(EPOCH FROM :start ::TIMESTAMP):: BIGINT
            , EXTRACT(EPOCH FROM :end ::TIMESTAMP) :: BIGINT
            , :dt*60*60::INT) t;
            """
    return query.format(func)

