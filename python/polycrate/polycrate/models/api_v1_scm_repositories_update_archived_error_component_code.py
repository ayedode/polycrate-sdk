from typing import Literal

ApiV1ScmRepositoriesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_SCM_REPOSITORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_scm_repositories_update_archived_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesUpdateArchivedErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
