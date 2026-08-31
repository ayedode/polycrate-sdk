from typing import Literal

ApiV1WorkspacesUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_WORKSPACES_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_workspaces_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
