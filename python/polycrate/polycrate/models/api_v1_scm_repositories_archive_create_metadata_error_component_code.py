from typing import Literal

ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_scm_repositories_archive_create_metadata_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
