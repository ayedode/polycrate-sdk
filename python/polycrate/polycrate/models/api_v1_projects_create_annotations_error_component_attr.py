from typing import Literal

ApiV1ProjectsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROJECTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_projects_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
