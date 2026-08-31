from typing import Literal

ApiV1AlertsArchiveCreateTitleErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_ARCHIVE_CREATE_TITLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsArchiveCreateTitleErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_archive_create_title_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateTitleErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_TITLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_TITLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
