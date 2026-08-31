from typing import Literal

ApiV1ScmRepositoriesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_SCM_REPOSITORIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_scm_repositories_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateCriticalityErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
