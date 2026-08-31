from typing import Literal

ApiV1WorkspacesPartialUpdateOwnerIdErrorComponentAttr = Literal["owner_id"]

API_V1_WORKSPACES_PARTIAL_UPDATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesPartialUpdateOwnerIdErrorComponentAttr
] = {
    "owner_id",
}


def check_api_v1_workspaces_partial_update_owner_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesPartialUpdateOwnerIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
