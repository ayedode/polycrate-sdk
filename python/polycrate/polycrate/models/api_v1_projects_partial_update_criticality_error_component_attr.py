from typing import Literal

ApiV1ProjectsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PROJECTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_projects_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
