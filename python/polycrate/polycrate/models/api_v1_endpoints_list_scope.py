from typing import Literal

ApiV1EndpointsListScope = Literal["system", "user"]

API_V1_ENDPOINTS_LIST_SCOPE_VALUES: set[ApiV1EndpointsListScope] = {
    "system",
    "user",
}


def check_api_v1_endpoints_list_scope(value: str) -> ApiV1EndpointsListScope:
    if value in API_V1_ENDPOINTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_SCOPE_VALUES!r}")
