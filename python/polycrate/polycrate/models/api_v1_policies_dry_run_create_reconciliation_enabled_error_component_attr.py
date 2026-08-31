from typing import Literal

ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_POLICIES_DRY_RUN_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_policies_dry_run_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
