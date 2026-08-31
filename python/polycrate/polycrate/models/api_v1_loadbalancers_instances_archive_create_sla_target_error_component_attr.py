from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_loadbalancers_instances_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
