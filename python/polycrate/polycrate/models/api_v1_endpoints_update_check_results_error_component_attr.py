from typing import Literal

ApiV1EndpointsUpdateCheckResultsErrorComponentAttr = Literal["check_results"]

API_V1_ENDPOINTS_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateCheckResultsErrorComponentAttr
] = {
    "check_results",
}


def check_api_v1_endpoints_update_check_results_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateCheckResultsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
