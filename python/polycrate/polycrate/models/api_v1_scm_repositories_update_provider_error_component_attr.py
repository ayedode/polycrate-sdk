from typing import Literal

ApiV1ScmRepositoriesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_SCM_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_scm_repositories_update_provider_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateProviderErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
