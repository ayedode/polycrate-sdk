from typing import Literal

ApiV1EndpointsUpdateCheckResultsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateCheckResultsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_update_check_results_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateCheckResultsErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
