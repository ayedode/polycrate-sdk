from typing import Literal

ApiV1EndpointsCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ENDPOINTS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_endpoints_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
