from typing import Literal

ApiV1EndpointsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_ENDPOINTS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsListCreatedAtErrorComponentAttr] = {
    "created_at",
}


def check_api_v1_endpoints_list_created_at_error_component_attr(
    value: str,
) -> ApiV1EndpointsListCreatedAtErrorComponentAttr:
    if value in API_V1_ENDPOINTS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
