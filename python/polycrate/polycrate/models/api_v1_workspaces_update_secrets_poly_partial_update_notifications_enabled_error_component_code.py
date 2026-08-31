from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_notifications_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
