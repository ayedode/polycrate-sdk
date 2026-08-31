from typing import Literal

ApiV1EndpointsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_endpoints_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
