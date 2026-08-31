from typing import Literal

ApiV1NotificationsSinksUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_NOTIFICATIONS_SINKS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_notifications_sinks_update_name_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateNameErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
