from typing import Literal

ApiV1ScmRepositoriesUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_SCM_REPOSITORIES_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_scm_repositories_update_credential_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateCredentialErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
