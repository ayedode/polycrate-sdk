from typing import Literal

ApiV1AlertsArchiveCreateGeneratorUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_ARCHIVE_CREATE_GENERATOR_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsArchiveCreateGeneratorUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_archive_create_generator_url_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateGeneratorUrlErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_GENERATOR_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_GENERATOR_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
