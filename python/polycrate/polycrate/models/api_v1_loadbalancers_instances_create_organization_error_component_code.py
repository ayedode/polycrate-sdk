from typing import Literal

ApiV1LoadbalancersInstancesCreateOrganizationErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_LOADBALANCERS_INSTANCES_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesCreateOrganizationErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_loadbalancers_instances_create_organization_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateOrganizationErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
