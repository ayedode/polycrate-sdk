from typing import Literal

ApiV1EndpointsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ENDPOINTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_endpoints_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
