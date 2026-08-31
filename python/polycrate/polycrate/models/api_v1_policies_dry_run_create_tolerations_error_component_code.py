from typing import Literal

ApiV1PoliciesDryRunCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_DRY_RUN_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_dry_run_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateTolerationsErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
