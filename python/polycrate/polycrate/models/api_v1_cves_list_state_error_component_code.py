from typing import Literal

ApiV1CvesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_CVES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_cves_list_state_error_component_code(value: str) -> ApiV1CvesListStateErrorComponentCode:
    if value in API_V1_CVES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
