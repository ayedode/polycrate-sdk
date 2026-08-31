from typing import Literal

ApiV1ArtifactPackagesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ARTIFACT_PACKAGES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_artifact_packages_create_archived_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateArchivedErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
