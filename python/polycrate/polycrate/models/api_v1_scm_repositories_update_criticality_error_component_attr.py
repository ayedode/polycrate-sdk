from typing import Literal

ApiV1ScmRepositoriesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_SCM_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_scm_repositories_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
