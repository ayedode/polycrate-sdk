from typing import Literal

ApiV1ScmRepositoriesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_SCM_REPOSITORIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_scm_repositories_update_kind_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateKindErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
