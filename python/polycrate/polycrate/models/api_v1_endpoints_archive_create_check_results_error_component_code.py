from typing import Literal

ApiV1EndpointsArchiveCreateCheckResultsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateCheckResultsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_archive_create_check_results_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateCheckResultsErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
