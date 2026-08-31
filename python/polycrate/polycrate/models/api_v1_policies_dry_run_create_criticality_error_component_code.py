from typing import Literal

ApiV1PoliciesDryRunCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_POLICIES_DRY_RUN_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_policies_dry_run_create_criticality_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateCriticalityErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
