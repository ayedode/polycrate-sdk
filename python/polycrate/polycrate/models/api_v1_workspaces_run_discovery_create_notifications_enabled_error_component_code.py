from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_notifications_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
