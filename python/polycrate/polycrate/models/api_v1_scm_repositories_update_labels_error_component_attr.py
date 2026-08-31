from typing import Literal

ApiV1ScmRepositoriesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_SCM_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_scm_repositories_update_labels_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateLabelsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
