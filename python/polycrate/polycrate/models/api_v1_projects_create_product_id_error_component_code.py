from typing import Literal

ApiV1ProjectsCreateProductIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PROJECTS_CREATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsCreateProductIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_projects_create_product_id_error_component_code(
    value: str,
) -> ApiV1ProjectsCreateProductIdErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
