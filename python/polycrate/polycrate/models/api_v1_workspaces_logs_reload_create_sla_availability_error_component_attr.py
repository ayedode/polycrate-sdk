from typing import Literal

ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_workspaces_logs_reload_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
