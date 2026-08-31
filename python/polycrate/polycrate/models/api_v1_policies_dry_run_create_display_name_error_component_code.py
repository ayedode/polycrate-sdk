from typing import Literal

ApiV1PoliciesDryRunCreateDisplayNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed", "unique"
]

API_V1_POLICIES_DRY_RUN_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateDisplayNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_policies_dry_run_create_display_name_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateDisplayNameErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
