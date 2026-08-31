from typing import Literal

ApiV1NotificationsSinksCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_NOTIFICATIONS_SINKS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_notifications_sinks_create_name_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateNameErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
