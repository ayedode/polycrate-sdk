from typing import Literal

ApiV1EndpointsDiscoverCreateCheckResultsErrorComponentAttr = Literal["check_results"]

API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateCheckResultsErrorComponentAttr
] = {
    "check_results",
}


def check_api_v1_endpoints_discover_create_check_results_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateCheckResultsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
