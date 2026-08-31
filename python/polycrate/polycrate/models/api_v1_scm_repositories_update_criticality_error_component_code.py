from typing import Literal

ApiV1ScmRepositoriesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_SCM_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_scm_repositories_update_criticality_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesUpdateCriticalityErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
