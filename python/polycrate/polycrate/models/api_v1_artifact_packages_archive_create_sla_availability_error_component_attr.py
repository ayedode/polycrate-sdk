from typing import Literal

ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_artifact_packages_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
