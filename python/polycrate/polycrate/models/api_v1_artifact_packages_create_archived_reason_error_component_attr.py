from typing import Literal

ApiV1ArtifactPackagesCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ARTIFACT_PACKAGES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_artifact_packages_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
