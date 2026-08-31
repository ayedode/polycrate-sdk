from typing import Literal

ApiV1OrganizationsUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_ORGANIZATIONS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_organizations_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateSloTargetErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
