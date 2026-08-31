from typing import Literal

ApiV1PrefixesUpdatePurposeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PREFIXES_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesUpdatePurposeErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_prefixes_update_purpose_error_component_code(
    value: str,
) -> ApiV1PrefixesUpdatePurposeErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
