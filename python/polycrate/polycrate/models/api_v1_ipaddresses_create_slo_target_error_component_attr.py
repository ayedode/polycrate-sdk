from typing import Literal

ApiV1IpaddressesCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_IPADDRESSES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_ipaddresses_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateSloTargetErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
