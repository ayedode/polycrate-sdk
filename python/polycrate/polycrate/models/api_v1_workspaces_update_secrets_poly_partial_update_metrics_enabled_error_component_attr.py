from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMetricsEnabledErrorComponentAttr = Literal["metrics_enabled"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMetricsEnabledErrorComponentAttr
] = {
    "metrics_enabled",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_metrics_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMetricsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
