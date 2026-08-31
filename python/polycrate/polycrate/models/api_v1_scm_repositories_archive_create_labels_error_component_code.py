from typing import Literal

ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_scm_repositories_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
