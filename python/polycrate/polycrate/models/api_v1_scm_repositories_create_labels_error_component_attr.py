from typing import Literal

ApiV1ScmRepositoriesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_SCM_REPOSITORIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_scm_repositories_create_labels_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateLabelsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
