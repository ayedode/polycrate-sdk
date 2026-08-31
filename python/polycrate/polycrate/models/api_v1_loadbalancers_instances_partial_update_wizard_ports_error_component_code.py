from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_instances_partial_update_wizard_ports_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
