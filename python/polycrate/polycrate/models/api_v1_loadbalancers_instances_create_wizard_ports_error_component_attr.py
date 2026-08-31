from typing import Literal

ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponentAttr = Literal["wizard_ports"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_WIZARD_PORTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponentAttr
] = {
    "wizard_ports",
}


def check_api_v1_loadbalancers_instances_create_wizard_ports_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_WIZARD_PORTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_WIZARD_PORTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
