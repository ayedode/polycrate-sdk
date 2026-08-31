from typing import Literal

ApiV1ScmRepositoriesPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_scm_repositories_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
