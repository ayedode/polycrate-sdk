from typing import Literal

ApiV1WorkspacesRepairCreateAlternativeNameErrorComponentAttr = Literal["alternative_name"]

API_V1_WORKSPACES_REPAIR_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateAlternativeNameErrorComponentAttr
] = {
    "alternative_name",
}


def check_api_v1_workspaces_repair_create_alternative_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateAlternativeNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
