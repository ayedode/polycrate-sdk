from typing import Literal

ApiV1AlertsDiscoverCreatePanelUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_DISCOVER_CREATE_PANEL_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreatePanelUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_discover_create_panel_url_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreatePanelUrlErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_PANEL_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_PANEL_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
