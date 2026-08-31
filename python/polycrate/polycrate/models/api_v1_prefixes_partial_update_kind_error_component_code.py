from typing import Literal

ApiV1PrefixesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PREFIXES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_prefixes_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateKindErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
