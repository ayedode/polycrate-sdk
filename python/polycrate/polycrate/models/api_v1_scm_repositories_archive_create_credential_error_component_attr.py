from typing import Literal

ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_scm_repositories_archive_create_credential_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
