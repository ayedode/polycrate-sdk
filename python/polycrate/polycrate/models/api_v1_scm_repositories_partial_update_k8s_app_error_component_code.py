from typing import Literal

ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_scm_repositories_partial_update_k8s_app_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
