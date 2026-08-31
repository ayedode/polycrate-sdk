from typing import Literal

ApiV1AlertsReconcileCreateMessageErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_RECONCILE_CREATE_MESSAGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsReconcileCreateMessageErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_reconcile_create_message_error_component_code(
    value: str,
) -> ApiV1AlertsReconcileCreateMessageErrorComponentCode:
    if value in API_V1_ALERTS_RECONCILE_CREATE_MESSAGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_MESSAGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
