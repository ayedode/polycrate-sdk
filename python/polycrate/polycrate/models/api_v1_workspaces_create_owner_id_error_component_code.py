from typing import Literal

ApiV1WorkspacesCreateOwnerIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_WORKSPACES_CREATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesCreateOwnerIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_workspaces_create_owner_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateOwnerIdErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
