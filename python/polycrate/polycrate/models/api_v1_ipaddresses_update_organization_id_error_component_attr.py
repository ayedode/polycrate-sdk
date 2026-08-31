from typing import Literal

ApiV1IpaddressesUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_IPADDRESSES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_ipaddresses_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
