from typing import Literal

ApiV1ScmRepositoriesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_SCM_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_scm_repositories_create_kind_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateKindErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
