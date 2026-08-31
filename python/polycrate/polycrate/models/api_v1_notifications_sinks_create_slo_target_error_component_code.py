from typing import Literal

ApiV1NotificationsSinksCreateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_NOTIFICATIONS_SINKS_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_notifications_sinks_create_slo_target_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateSloTargetErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
