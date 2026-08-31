from typing import Literal

ApiV1ArtifactsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_artifacts_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
