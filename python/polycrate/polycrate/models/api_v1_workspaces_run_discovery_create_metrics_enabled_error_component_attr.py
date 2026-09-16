from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateMetricsEnabledErrorComponentAttr = Literal["metrics_enabled"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateMetricsEnabledErrorComponentAttr
] = {
    "metrics_enabled",
}


def check_api_v1_workspaces_run_discovery_create_metrics_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateMetricsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
