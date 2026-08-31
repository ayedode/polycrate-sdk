from typing import Literal

ApiV1AlertsPartialUpdateExternalUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_PARTIAL_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateExternalUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_partial_update_external_url_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateExternalUrlErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
