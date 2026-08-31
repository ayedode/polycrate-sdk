from typing import Literal

ApiV1ArtifactPackagesUpdateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_ARTIFACT_PACKAGES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_artifact_packages_update_archived_by_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateArchivedByErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
