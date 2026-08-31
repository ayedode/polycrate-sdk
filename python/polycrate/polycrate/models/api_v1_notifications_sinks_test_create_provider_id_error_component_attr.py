from typing import Literal

ApiV1NotificationsSinksTestCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_notifications_sinks_test_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateProviderIdErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
