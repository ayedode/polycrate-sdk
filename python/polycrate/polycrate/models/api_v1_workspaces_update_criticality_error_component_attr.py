from typing import Literal

ApiV1WorkspacesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_update_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
