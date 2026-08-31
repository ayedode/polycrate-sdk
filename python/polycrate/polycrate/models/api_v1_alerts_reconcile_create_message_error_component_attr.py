from typing import Literal

ApiV1AlertsReconcileCreateMessageErrorComponentAttr = Literal["message"]

API_V1_ALERTS_RECONCILE_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateMessageErrorComponentAttr
] = {
    "message",
}


def check_api_v1_alerts_reconcile_create_message_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateMessageErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
