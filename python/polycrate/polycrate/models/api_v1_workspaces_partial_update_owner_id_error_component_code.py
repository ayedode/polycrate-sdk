from typing import Literal

ApiV1WorkspacesPartialUpdateOwnerIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_WORKSPACES_PARTIAL_UPDATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateOwnerIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_workspaces_partial_update_owner_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateOwnerIdErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
