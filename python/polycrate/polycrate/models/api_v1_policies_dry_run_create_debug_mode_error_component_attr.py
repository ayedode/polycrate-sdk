from typing import Literal

ApiV1PoliciesDryRunCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_POLICIES_DRY_RUN_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_policies_dry_run_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateDebugModeErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
