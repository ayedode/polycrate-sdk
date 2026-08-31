from typing import Literal

ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_artifact_packages_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
