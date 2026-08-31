from typing import Literal

ApiV1PoliciesDryRunCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_POLICIES_DRY_RUN_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_policies_dry_run_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
