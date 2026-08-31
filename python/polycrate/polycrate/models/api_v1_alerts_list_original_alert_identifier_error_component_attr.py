from typing import Literal

ApiV1AlertsListOriginalAlertIdentifierErrorComponentAttr = Literal["original_alert_identifier"]

API_V1_ALERTS_LIST_ORIGINAL_ALERT_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsListOriginalAlertIdentifierErrorComponentAttr
] = {
    "original_alert_identifier",
}


def check_api_v1_alerts_list_original_alert_identifier_error_component_attr(
    value: str,
) -> ApiV1AlertsListOriginalAlertIdentifierErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_ORIGINAL_ALERT_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_ORIGINAL_ALERT_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
