from typing import Literal

ApiV1ProjectsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROJECTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_projects_update_annotations_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
