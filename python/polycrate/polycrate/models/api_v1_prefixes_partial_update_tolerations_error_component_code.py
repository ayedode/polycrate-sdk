from typing import Literal

ApiV1PrefixesPartialUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_partial_update_tolerations_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateTolerationsErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
