from typing import Literal

ApiV1WorkspacesCheckCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_check_create_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
