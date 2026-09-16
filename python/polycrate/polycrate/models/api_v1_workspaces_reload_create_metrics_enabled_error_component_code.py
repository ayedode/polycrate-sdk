from typing import Literal

ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RELOAD_CREATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_reload_create_metrics_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
