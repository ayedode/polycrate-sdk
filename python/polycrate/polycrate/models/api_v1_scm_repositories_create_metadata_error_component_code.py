from typing import Literal

ApiV1ScmRepositoriesCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_SCM_REPOSITORIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_scm_repositories_create_metadata_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesCreateMetadataErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
