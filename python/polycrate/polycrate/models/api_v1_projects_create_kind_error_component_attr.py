from typing import Literal

ApiV1ProjectsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PROJECTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_projects_create_kind_error_component_attr(value: str) -> ApiV1ProjectsCreateKindErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
