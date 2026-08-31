from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponentAttr = Literal["external_traffic_policy"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponentAttr
] = {
    "external_traffic_policy",
}


def check_api_v1_loadbalancers_regions_archive_create_external_traffic_policy_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_EXTERNAL_TRAFFIC_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
