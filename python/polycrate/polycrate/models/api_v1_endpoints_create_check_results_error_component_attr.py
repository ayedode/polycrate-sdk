from typing import Literal

ApiV1EndpointsCreateCheckResultsErrorComponentAttr = Literal["check_results"]

API_V1_ENDPOINTS_CREATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateCheckResultsErrorComponentAttr
] = {
    "check_results",
}


def check_api_v1_endpoints_create_check_results_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateCheckResultsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
