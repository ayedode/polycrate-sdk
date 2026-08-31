from typing import Literal

ApiV1PrefixesPartialUpdatePurposeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PREFIXES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdatePurposeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_prefixes_partial_update_purpose_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdatePurposeErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
