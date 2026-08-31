from typing import Literal

ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_scm_repositories_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
