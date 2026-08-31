from typing import Literal

ApiV1PoliciesDryRunCreateKindsSelectorErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_DRY_RUN_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateKindsSelectorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_dry_run_create_kinds_selector_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateKindsSelectorErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
