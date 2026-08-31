from typing import Literal

ApiV1PrefixesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
