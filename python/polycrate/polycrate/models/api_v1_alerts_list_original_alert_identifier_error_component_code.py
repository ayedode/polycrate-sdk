from typing import Literal

ApiV1AlertsListOriginalAlertIdentifierErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ALERTS_LIST_ORIGINAL_ALERT_IDENTIFIER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsListOriginalAlertIdentifierErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_alerts_list_original_alert_identifier_error_component_code(
    value: str,
) -> ApiV1AlertsListOriginalAlertIdentifierErrorComponentCode:
    if value in API_V1_ALERTS_LIST_ORIGINAL_ALERT_IDENTIFIER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_ORIGINAL_ALERT_IDENTIFIER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
