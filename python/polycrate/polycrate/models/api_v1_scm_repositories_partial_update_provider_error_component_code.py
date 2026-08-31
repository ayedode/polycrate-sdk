from typing import Literal

ApiV1ScmRepositoriesPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_scm_repositories_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateProviderErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
