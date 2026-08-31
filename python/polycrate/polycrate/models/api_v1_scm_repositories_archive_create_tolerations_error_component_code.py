from typing import Literal

ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_scm_repositories_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
