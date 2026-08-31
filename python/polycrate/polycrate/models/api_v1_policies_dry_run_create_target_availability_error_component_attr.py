from typing import Literal

ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_POLICIES_DRY_RUN_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_policies_dry_run_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
