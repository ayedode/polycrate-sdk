from typing import Literal

ApiV1PoliciesDryRunCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_POLICIES_DRY_RUN_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_policies_dry_run_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateSlaTargetErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
