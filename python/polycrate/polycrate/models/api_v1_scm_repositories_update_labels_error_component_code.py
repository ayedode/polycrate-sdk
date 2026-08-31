from typing import Literal

ApiV1ScmRepositoriesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_SCM_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_scm_repositories_update_labels_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesUpdateLabelsErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
