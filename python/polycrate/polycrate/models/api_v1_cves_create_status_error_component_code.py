from typing import Literal

ApiV1CvesCreateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CVES_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesCreateStatusErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_cves_create_status_error_component_code(value: str) -> ApiV1CvesCreateStatusErrorComponentCode:
    if value in API_V1_CVES_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
