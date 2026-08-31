from typing import Literal

ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponentAttr = Literal["observability_metrics"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponentAttr
] = {
    "observability_metrics",
}


def check_api_v1_organizations_archive_create_observability_metrics_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
