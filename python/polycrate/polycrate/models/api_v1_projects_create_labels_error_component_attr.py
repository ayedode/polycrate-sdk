from typing import Literal

ApiV1ProjectsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PROJECTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_projects_create_labels_error_component_attr(value: str) -> ApiV1ProjectsCreateLabelsErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
