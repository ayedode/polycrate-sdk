from typing import Literal

ApiV1WorkspacesRepairCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_REPAIR_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_repair_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
