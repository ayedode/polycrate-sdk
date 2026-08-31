from typing import Literal

ApiV1PrefixesUpdateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PREFIXES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesUpdateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_prefixes_update_archived_reason_error_component_code(
    value: str,
) -> ApiV1PrefixesUpdateArchivedReasonErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
