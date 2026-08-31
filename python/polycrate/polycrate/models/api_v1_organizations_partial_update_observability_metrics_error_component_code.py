from typing import Literal

ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_partial_update_observability_metrics_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
