from typing import Literal

ApiV1ScmRepositoriesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_SCM_REPOSITORIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_scm_repositories_create_provider_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateProviderErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
