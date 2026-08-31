from typing import Literal

ApiV1ProjectsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROJECTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_projects_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
