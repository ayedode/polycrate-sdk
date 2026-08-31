from typing import Literal

ApiV1WorkspacesCreateOwnerIdErrorComponentAttr = Literal["owner_id"]

API_V1_WORKSPACES_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreateOwnerIdErrorComponentAttr] = {
    "owner_id",
}


def check_api_v1_workspaces_create_owner_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateOwnerIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
