from typing import Literal

ApiV1ScmRepositoriesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_SCM_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_scm_repositories_create_kind_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesCreateKindErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
