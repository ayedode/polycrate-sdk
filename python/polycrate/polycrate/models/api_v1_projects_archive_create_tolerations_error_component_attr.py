from typing import Literal

ApiV1ProjectsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROJECTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_projects_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
