from typing import Literal

ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_WORKSPACES_DISCOVER_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_workspaces_discover_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
