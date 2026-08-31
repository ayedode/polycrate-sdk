from typing import Literal

ApiV1ProjectsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PROJECTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_projects_update_archived_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateArchivedErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
