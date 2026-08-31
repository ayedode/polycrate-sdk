from typing import Literal

ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_reconcile_create_platform_service_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
