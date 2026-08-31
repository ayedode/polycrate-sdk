from typing import Literal

ApiV1PrefixesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PREFIXES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_prefixes_update_kind_error_component_code(value: str) -> ApiV1PrefixesUpdateKindErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
