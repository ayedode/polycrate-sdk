from typing import Literal

ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_notifications_sinks_test_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
