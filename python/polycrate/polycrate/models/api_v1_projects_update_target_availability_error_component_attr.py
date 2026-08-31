from typing import Literal

ApiV1ProjectsUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PROJECTS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_projects_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
