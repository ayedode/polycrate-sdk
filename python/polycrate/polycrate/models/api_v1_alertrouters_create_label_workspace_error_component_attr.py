from typing import Literal

ApiV1AlertroutersCreateLabelWorkspaceErrorComponentAttr = Literal["label_workspace"]

API_V1_ALERTROUTERS_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateLabelWorkspaceErrorComponentAttr
] = {
    "label_workspace",
}


def check_api_v1_alertrouters_create_label_workspace_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateLabelWorkspaceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
