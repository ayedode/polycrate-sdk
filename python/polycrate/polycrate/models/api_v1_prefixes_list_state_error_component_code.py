from typing import Literal

ApiV1PrefixesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_PREFIXES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_prefixes_list_state_error_component_code(value: str) -> ApiV1PrefixesListStateErrorComponentCode:
    if value in API_V1_PREFIXES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
