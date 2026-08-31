from typing import Literal

ApiV1PrefixesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_update_tolerations_error_component_code(
    value: str,
) -> ApiV1PrefixesUpdateTolerationsErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
