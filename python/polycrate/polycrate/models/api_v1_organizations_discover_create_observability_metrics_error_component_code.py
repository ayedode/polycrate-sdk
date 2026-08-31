from typing import Literal

ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_discover_create_observability_metrics_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
