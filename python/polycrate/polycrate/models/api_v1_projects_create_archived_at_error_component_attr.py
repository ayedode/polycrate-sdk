from typing import Literal

ApiV1ProjectsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PROJECTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsCreateArchivedAtErrorComponentAttr] = {
    "archived_at",
}


def check_api_v1_projects_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
