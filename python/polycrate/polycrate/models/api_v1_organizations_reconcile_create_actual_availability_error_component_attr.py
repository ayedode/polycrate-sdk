from typing import Literal

ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_organizations_reconcile_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
