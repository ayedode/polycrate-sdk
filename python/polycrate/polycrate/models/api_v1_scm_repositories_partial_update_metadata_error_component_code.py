from typing import Literal

ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_scm_repositories_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
