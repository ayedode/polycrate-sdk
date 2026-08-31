from typing import Literal

ApiV1AlertsCreateDashboardUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_CREATE_DASHBOARD_URL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsCreateDashboardUrlErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_create_dashboard_url_error_component_code(
    value: str,
) -> ApiV1AlertsCreateDashboardUrlErrorComponentCode:
    if value in API_V1_ALERTS_CREATE_DASHBOARD_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_DASHBOARD_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
