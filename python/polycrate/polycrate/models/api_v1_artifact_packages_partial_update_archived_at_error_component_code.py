from typing import Literal

ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_artifact_packages_partial_update_archived_at_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
