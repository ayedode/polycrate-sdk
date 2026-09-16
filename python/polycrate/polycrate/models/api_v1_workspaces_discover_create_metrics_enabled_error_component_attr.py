from typing import Literal

ApiV1WorkspacesDiscoverCreateMetricsEnabledErrorComponentAttr = Literal["metrics_enabled"]

API_V1_WORKSPACES_DISCOVER_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateMetricsEnabledErrorComponentAttr
] = {
    "metrics_enabled",
}


def check_api_v1_workspaces_discover_create_metrics_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateMetricsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
