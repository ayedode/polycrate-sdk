from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_organization_products_list_created_at_error_component import (
        ApiV1PricingOrganizationProductsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_created_by_component_error_component import (
        ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_kind_error_component import (
        ApiV1PricingOrganizationProductsListKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_name_error_component import (
        ApiV1PricingOrganizationProductsListNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_product_error_component import (
        ApiV1PricingOrganizationProductsListProductErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_product_kind_error_component import (
        ApiV1PricingOrganizationProductsListProductKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_scope_error_component import (
        ApiV1PricingOrganizationProductsListScopeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_state_error_component import (
        ApiV1PricingOrganizationProductsListStateErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_list_updated_at_error_component import (
        ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingOrganizationProductsListValidationError")


@_attrs_define
class ApiV1PricingOrganizationProductsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingOrganizationProductsListCreatedAtErrorComponent |
            ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent |
            ApiV1PricingOrganizationProductsListKindErrorComponent | ApiV1PricingOrganizationProductsListNameErrorComponent
            | ApiV1PricingOrganizationProductsListProductErrorComponent |
            ApiV1PricingOrganizationProductsListProductKindErrorComponent |
            ApiV1PricingOrganizationProductsListScopeErrorComponent |
            ApiV1PricingOrganizationProductsListStateErrorComponent |
            ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingOrganizationProductsListCreatedAtErrorComponent
        | ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent
        | ApiV1PricingOrganizationProductsListKindErrorComponent
        | ApiV1PricingOrganizationProductsListNameErrorComponent
        | ApiV1PricingOrganizationProductsListProductErrorComponent
        | ApiV1PricingOrganizationProductsListProductKindErrorComponent
        | ApiV1PricingOrganizationProductsListScopeErrorComponent
        | ApiV1PricingOrganizationProductsListStateErrorComponent
        | ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_organization_products_list_created_at_error_component import (
            ApiV1PricingOrganizationProductsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_created_by_component_error_component import (
            ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_kind_error_component import (
            ApiV1PricingOrganizationProductsListKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_name_error_component import (
            ApiV1PricingOrganizationProductsListNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_product_error_component import (
            ApiV1PricingOrganizationProductsListProductErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_scope_error_component import (
            ApiV1PricingOrganizationProductsListScopeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_state_error_component import (
            ApiV1PricingOrganizationProductsListStateErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_updated_at_error_component import (
            ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingOrganizationProductsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsListProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_pricing_organization_products_list_created_at_error_component import (
            ApiV1PricingOrganizationProductsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_created_by_component_error_component import (
            ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_kind_error_component import (
            ApiV1PricingOrganizationProductsListKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_name_error_component import (
            ApiV1PricingOrganizationProductsListNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_product_error_component import (
            ApiV1PricingOrganizationProductsListProductErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_product_kind_error_component import (
            ApiV1PricingOrganizationProductsListProductKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_scope_error_component import (
            ApiV1PricingOrganizationProductsListScopeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_state_error_component import (
            ApiV1PricingOrganizationProductsListStateErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_list_updated_at_error_component import (
            ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingOrganizationProductsListCreatedAtErrorComponent
                | ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent
                | ApiV1PricingOrganizationProductsListKindErrorComponent
                | ApiV1PricingOrganizationProductsListNameErrorComponent
                | ApiV1PricingOrganizationProductsListProductErrorComponent
                | ApiV1PricingOrganizationProductsListProductKindErrorComponent
                | ApiV1PricingOrganizationProductsListScopeErrorComponent
                | ApiV1PricingOrganizationProductsListStateErrorComponent
                | ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_0 = (
                        ApiV1PricingOrganizationProductsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_1 = (
                        ApiV1PricingOrganizationProductsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_2 = (
                        ApiV1PricingOrganizationProductsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_3 = (
                        ApiV1PricingOrganizationProductsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_4 = (
                        ApiV1PricingOrganizationProductsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_5 = (
                        ApiV1PricingOrganizationProductsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_6 = (
                        ApiV1PricingOrganizationProductsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_list_error_type_7 = (
                        ApiV1PricingOrganizationProductsListProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_organization_products_list_error_type_8 = (
                    ApiV1PricingOrganizationProductsListProductKindErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_organization_products_list_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_organization_products_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_organization_products_list_validation_error.additional_properties = d
        return api_v1_pricing_organization_products_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
