from typing import Literal

ApiV1ScmRepositoriesUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_SCM_REPOSITORIES_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesUpdateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_scm_repositories_update_credential_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesUpdateCredentialErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
