from typing import Literal

ApiV1PoliciesDryRunCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICIES_DRY_RUN_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policies_dry_run_create_kind_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateKindErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
