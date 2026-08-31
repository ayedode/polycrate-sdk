from typing import Literal

ApiV1WorkspacesArchiveCreateOnPremiseErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_ARCHIVE_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateOnPremiseErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_archive_create_on_premise_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateOnPremiseErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
