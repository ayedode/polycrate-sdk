from typing import Literal

ApiV1CvesListStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_CVES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesListStatusErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_cves_list_status_error_component_code(value: str) -> ApiV1CvesListStatusErrorComponentCode:
    if value in API_V1_CVES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
