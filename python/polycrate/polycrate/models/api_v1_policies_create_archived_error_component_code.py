from typing import Literal

ApiV1PoliciesCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesCreateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_policies_create_archived_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateArchivedErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
