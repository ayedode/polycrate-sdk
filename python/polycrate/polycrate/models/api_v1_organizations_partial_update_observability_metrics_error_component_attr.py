from typing import Literal

ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponentAttr = Literal["observability_metrics"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponentAttr
] = {
    "observability_metrics",
}


def check_api_v1_organizations_partial_update_observability_metrics_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
