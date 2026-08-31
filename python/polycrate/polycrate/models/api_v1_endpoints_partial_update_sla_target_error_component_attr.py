from typing import Literal

ApiV1EndpointsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_endpoints_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
