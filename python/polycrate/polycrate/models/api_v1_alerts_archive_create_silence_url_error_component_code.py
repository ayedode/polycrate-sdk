from typing import Literal

ApiV1AlertsArchiveCreateSilenceUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsArchiveCreateSilenceUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_archive_create_silence_url_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateSilenceUrlErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
