from typing import Literal

ApiV1PopsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_POPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsListUpdatedAtErrorComponentCode] = {
    "invalid",
}


def check_api_v1_pops_list_updated_at_error_component_code(value: str) -> ApiV1PopsListUpdatedAtErrorComponentCode:
    if value in API_V1_POPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
