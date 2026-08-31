from typing import Literal

ApiV1ScmRepositoriesCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_SCM_REPOSITORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_scm_repositories_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateProviderIdErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
