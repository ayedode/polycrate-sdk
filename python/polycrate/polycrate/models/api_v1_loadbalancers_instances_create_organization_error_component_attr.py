from typing import Literal

ApiV1LoadbalancersInstancesCreateOrganizationErrorComponentAttr = Literal["organization"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_loadbalancers_instances_create_organization_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateOrganizationErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
