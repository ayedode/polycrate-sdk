from typing import Literal

ApiV1WorkspacesPartialUpdateMetricsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateMetricsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_partial_update_metrics_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateMetricsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
