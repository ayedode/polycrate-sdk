from typing import Literal

ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_scm_repositories_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
