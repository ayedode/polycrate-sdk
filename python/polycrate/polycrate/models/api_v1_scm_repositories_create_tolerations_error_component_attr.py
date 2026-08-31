from typing import Literal

ApiV1ScmRepositoriesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_SCM_REPOSITORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_scm_repositories_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateTolerationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
