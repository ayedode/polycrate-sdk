from typing import Literal

ApiV1NotificationsSinksUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_notifications_sinks_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateProviderIdErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
