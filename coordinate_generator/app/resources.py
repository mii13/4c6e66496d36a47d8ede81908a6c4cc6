from flask import request
from .common import sql_to_python, ApiException, BaseResource
from .utils import get_query_str
from .schemas import CoordinateRequestSchema


class CoordinatesResource(BaseResource):
    schema_cls = CoordinateRequestSchema

    def post(self):
        req_data = request.get_json(force=True)
        if req_data is None:
            raise ApiException(401, "You missed json attributes")
        params = self._get_deserialized_data(req_data)

        return sql_to_python(get_query_str(params["func"]),
                             params={"start": params["start"], "end": params["end"], "dt": params["dt"]})
