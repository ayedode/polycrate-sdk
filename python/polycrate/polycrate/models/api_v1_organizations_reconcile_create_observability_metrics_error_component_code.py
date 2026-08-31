from typing import Literal

ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_reconcile_create_observability_metrics_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
