from typing import Literal

ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_notifications_sinks_partial_update_provider_id_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
