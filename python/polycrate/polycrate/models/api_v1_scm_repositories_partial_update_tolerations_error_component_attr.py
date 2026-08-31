from typing import Literal

ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_scm_repositories_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
