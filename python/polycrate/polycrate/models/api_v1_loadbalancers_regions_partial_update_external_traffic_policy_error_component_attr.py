from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponentAttr = Literal["external_traffic_policy"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponentAttr
] = {
    "external_traffic_policy",
}


def check_api_v1_loadbalancers_regions_partial_update_external_traffic_policy_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
