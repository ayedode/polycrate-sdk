from typing import Literal

ApiV1RegionsArchiveCreateStateReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_REGIONS_ARCHIVE_CREATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsArchiveCreateStateReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_regions_archive_create_state_reason_error_component_code(
    value: str,
) -> ApiV1RegionsArchiveCreateStateReasonErrorComponentCode:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
