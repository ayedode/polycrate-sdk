from typing import Literal

ApiV1ProjectsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PROJECTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_projects_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
