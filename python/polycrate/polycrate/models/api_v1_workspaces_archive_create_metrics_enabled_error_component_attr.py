from typing import Literal

ApiV1WorkspacesArchiveCreateMetricsEnabledErrorComponentAttr = Literal["metrics_enabled"]

API_V1_WORKSPACES_ARCHIVE_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateMetricsEnabledErrorComponentAttr
] = {
    "metrics_enabled",
}


def check_api_v1_workspaces_archive_create_metrics_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateMetricsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
