from typing import Literal

ApiV1PoliciesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesUpdateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_policies_update_archived_error_component_code(
    value: str,
) -> ApiV1PoliciesUpdateArchivedErrorComponentCode:
    if value in API_V1_POLICIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
