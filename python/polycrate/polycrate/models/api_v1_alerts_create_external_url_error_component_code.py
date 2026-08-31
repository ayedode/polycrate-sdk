from typing import Literal

ApiV1AlertsCreateExternalUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_CREATE_EXTERNAL_URL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsCreateExternalUrlErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_create_external_url_error_component_code(
    value: str,
) -> ApiV1AlertsCreateExternalUrlErrorComponentCode:
    if value in API_V1_ALERTS_CREATE_EXTERNAL_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_EXTERNAL_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
