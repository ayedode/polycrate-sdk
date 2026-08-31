from typing import Literal

ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponentAttr = Literal["external_traffic_policy"]

API_V1_LOADBALANCERS_REGIONS_CREATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponentAttr
] = {
    "external_traffic_policy",
}


def check_api_v1_loadbalancers_regions_create_external_traffic_policy_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
