from typing import Literal

ApiV1OrganizationsReconcileCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_organizations_reconcile_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateSloTargetErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
