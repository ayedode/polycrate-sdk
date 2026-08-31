from typing import Literal

ApiV1CredentialsReconcileCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_CREDENTIALS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_credentials_reconcile_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateSlaTargetErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
