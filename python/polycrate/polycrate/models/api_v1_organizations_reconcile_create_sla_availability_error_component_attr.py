from typing import Literal

ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_organizations_reconcile_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
