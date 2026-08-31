from typing import Literal

ApiV1ProjectsArchiveCreateStartDateErrorComponentAttr = Literal["start_date"]

API_V1_PROJECTS_ARCHIVE_CREATE_START_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateStartDateErrorComponentAttr
] = {
    "start_date",
}


def check_api_v1_projects_archive_create_start_date_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateStartDateErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_START_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_START_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
