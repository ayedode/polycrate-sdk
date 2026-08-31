from typing import Literal

ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_scm_repositories_archive_create_credential_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
