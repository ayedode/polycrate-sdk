from typing import Literal

ApiV1ProjectsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PROJECTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_projects_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
