from datetime import datetime
from flask_restful import Resource
from flask.json import JSONEncoder
from marshmallow import Schema
from app.extensions import db


class ApiException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.message = msg

    def __repr__(self):
        return 'Error %s: %s' % (self.code, self.message)

    def __str__(self):
        return 'Error %s: %s' % (self.code, self.message)


def wrap_response_hook(f):

    def _wrap_resp(data, error=None):
        result = {"ok": True, "error_code": None, "message": None, "result": None}
        if error:
            result["ok"] = False
            result["error_code"] = data.code
            result["message"] = data.message
        else:
            result['result'] = data
        return result

    def wrap(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except ApiException as e:
            return _wrap_resp(e, error=True)
        else:
            return _wrap_resp(result)
    return wrap


class BaseResource(Resource):
    method_decorators = [wrap_response_hook]
    schema_cls = None

    def _get_deserialized_data(self, data, context=None, partial_load=False,
                               raise_http_error=False, schema_cls=None):
        if schema_cls is None:
            schema_cls = self.schema_cls
        if schema_cls is None and not issubclass(schema_cls, Schema):
            raise AssertionError(
                ('schema_cls should be provided and be subclass of '
                 'marshmallow.Schema')
            )
        schema = schema_cls()
        schema.context = context if context else {}
        deserialized_schema = schema.load(data, partial=partial_load)
        if deserialized_schema.errors:
            if raise_http_error:
                raise ApiException(400, deserialized_schema.errors)
            raise ApiException(400, deserialized_schema.errors)
        return deserialized_schema.data


def _dict_fetchall(fetched_result, columns):
    """Return all rows from a cursor as a dict"""

    data = [
        dict(zip(columns, row))
        for row in fetched_result
    ]

    return data


def _list_fetchall(fetched_result):
    """Return all rows from a cursor as a dict"""

    return [list(row) for row in fetched_result]

def sql_to_python(query, params=None):
    """ do query """

    result_sql = db.session.execute(query, params=params)
    # columns = result_sql.keys()

    db.session.commit()

    # fetched_result = result_sql.fetchall()

    return _list_fetchall(result_sql)


class CustomJSONEncoder(JSONEncoder):

    def default(self, o):
        """
        Extend Flask-JSONEncoder to handle datetime object properly
        """
        if isinstance(o, datetime):
            return o.isoformat()
        return super(CustomJSONEncoder, self).default(o)
