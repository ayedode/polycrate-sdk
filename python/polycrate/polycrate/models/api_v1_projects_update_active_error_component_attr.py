from typing import Literal

ApiV1ProjectsUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_PROJECTS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsUpdateActiveErrorComponentAttr] = {
    "active",
}


def check_api_v1_projects_update_active_error_component_attr(value: str) -> ApiV1ProjectsUpdateActiveErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
