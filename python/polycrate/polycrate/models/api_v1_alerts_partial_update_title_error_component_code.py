from typing import Literal

ApiV1AlertsPartialUpdateTitleErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsPartialUpdateTitleErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_partial_update_title_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateTitleErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
