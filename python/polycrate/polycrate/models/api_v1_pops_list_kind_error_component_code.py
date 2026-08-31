from typing import Literal

ApiV1PopsListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_POPS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsListKindErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_pops_list_kind_error_component_code(value: str) -> ApiV1PopsListKindErrorComponentCode:
    if value in API_V1_POPS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
