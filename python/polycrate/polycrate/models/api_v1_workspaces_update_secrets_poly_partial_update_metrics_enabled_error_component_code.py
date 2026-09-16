from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMetricsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMetricsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_metrics_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMetricsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_METRICS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
