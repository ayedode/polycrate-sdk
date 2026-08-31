from typing import Literal

ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponentAttr = Literal["cached_metrics_updated_at"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponentAttr
] = {
    "cached_metrics_updated_at",
}


def check_api_v1_organizations_archive_create_cached_metrics_updated_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
