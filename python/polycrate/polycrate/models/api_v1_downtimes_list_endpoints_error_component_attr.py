from typing import Literal

ApiV1DowntimesListEndpointsErrorComponentAttr = Literal["endpoints"]

API_V1_DOWNTIMES_LIST_ENDPOINTS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesListEndpointsErrorComponentAttr] = {
    "endpoints",
}


def check_api_v1_downtimes_list_endpoints_error_component_attr(
    value: str,
) -> ApiV1DowntimesListEndpointsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_ENDPOINTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_ENDPOINTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
