from typing import Literal

ApiV1ProjectsPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_PROJECTS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_projects_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
