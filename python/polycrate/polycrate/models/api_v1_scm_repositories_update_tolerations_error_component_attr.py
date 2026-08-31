from typing import Literal

ApiV1ScmRepositoriesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_SCM_REPOSITORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_scm_repositories_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
