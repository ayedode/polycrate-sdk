from typing import Literal

ApiV1DowntimesListUntilErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesListUntilErrorComponentCode] = {
    "invalid",
}


def check_api_v1_downtimes_list_until_error_component_code(value: str) -> ApiV1DowntimesListUntilErrorComponentCode:
    if value in API_V1_DOWNTIMES_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
