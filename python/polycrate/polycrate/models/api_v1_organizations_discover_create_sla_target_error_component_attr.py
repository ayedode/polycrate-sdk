from typing import Literal

ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_organizations_discover_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
