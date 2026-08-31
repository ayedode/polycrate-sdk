from typing import Literal

ApiV1EndpointsPartialUpdateCheckResultsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateCheckResultsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_partial_update_check_results_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateCheckResultsErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
