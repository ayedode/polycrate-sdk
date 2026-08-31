from typing import Literal

ApiV1PoliciesDryRunCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_dry_run_create_archived_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateArchivedErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
