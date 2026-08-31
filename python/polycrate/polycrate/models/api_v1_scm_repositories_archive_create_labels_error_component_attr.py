from typing import Literal

ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_scm_repositories_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
