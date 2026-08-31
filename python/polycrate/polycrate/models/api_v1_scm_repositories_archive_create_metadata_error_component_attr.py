from typing import Literal

ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_scm_repositories_archive_create_metadata_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
