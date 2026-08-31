from typing import Literal

ApiV1PoliciesDryRunCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_POLICIES_DRY_RUN_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_policies_dry_run_create_sla_target_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateSlaTargetErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
