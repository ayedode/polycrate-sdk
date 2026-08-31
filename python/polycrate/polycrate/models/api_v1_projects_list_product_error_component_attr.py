from typing import Literal

ApiV1ProjectsListProductErrorComponentAttr = Literal["product"]

API_V1_PROJECTS_LIST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsListProductErrorComponentAttr] = {
    "product",
}


def check_api_v1_projects_list_product_error_component_attr(value: str) -> ApiV1ProjectsListProductErrorComponentAttr:
    if value in API_V1_PROJECTS_LIST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
