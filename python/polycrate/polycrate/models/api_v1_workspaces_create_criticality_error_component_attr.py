from typing import Literal

ApiV1WorkspacesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_create_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
