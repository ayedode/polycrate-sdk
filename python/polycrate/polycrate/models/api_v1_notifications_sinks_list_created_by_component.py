from typing import Literal

ApiV1NotificationsSinksListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_NOTIFICATIONS_SINKS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1NotificationsSinksListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_notifications_sinks_list_created_by_component(
    value: str,
) -> ApiV1NotificationsSinksListCreatedByComponent:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
