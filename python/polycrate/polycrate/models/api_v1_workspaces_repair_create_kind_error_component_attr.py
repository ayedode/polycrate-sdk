from typing import Literal

ApiV1WorkspacesRepairCreateKindErrorComponentAttr = Literal["kind"]

API_V1_WORKSPACES_REPAIR_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_workspaces_repair_create_kind_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateKindErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
