from typing import Literal

ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_workspaces_logs_reload_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
