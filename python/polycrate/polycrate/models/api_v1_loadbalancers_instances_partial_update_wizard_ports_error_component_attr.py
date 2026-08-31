from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponentAttr = Literal["wizard_ports"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponentAttr
] = {
    "wizard_ports",
}


def check_api_v1_loadbalancers_instances_partial_update_wizard_ports_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_WIZARD_PORTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
