from typing import Literal

ApiV1WorkspacesArchiveCreateOwnerIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_WORKSPACES_ARCHIVE_CREATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateOwnerIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_workspaces_archive_create_owner_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateOwnerIdErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_OWNER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
