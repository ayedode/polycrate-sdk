from typing import Literal

ApiV1LoadbalancersInstancesUpdateWizardPortsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesUpdateWizardPortsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_instances_update_wizard_ports_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdateWizardPortsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
