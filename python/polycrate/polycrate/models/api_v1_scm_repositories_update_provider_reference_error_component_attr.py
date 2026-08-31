from typing import Literal

ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_SCM_REPOSITORIES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_scm_repositories_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
