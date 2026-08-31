from typing import Literal

ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponentAttr = Literal["observability_metrics"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponentAttr
] = {
    "observability_metrics",
}


def check_api_v1_organizations_icon_upload_create_observability_metrics_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_OBSERVABILITY_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
