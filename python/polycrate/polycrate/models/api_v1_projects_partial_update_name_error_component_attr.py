from typing import Literal

ApiV1ProjectsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PROJECTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_projects_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
