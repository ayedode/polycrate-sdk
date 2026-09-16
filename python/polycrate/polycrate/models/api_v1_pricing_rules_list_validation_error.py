from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_rules_list_created_at_error_component import (
        ApiV1PricingRulesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_pricing_rules_list_created_by_component_error_component import (
        ApiV1PricingRulesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_pricing_rules_list_kind_error_component import ApiV1PricingRulesListKindErrorComponent
    from ..models.api_v1_pricing_rules_list_name_error_component import ApiV1PricingRulesListNameErrorComponent
    from ..models.api_v1_pricing_rules_list_product_kind_error_component import (
        ApiV1PricingRulesListProductKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_list_scope_error_component import ApiV1PricingRulesListScopeErrorComponent
    from ..models.api_v1_pricing_rules_list_state_error_component import ApiV1PricingRulesListStateErrorComponent
    from ..models.api_v1_pricing_rules_list_updated_at_error_component import (
        ApiV1PricingRulesListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingRulesListValidationError")


@_attrs_define
class ApiV1PricingRulesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingRulesListCreatedAtErrorComponent |
            ApiV1PricingRulesListCreatedByComponentErrorComponent | ApiV1PricingRulesListKindErrorComponent |
            ApiV1PricingRulesListNameErrorComponent | ApiV1PricingRulesListProductKindErrorComponent |
            ApiV1PricingRulesListScopeErrorComponent | ApiV1PricingRulesListStateErrorComponent |
            ApiV1PricingRulesListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingRulesListCreatedAtErrorComponent
        | ApiV1PricingRulesListCreatedByComponentErrorComponent
        | ApiV1PricingRulesListKindErrorComponent
        | ApiV1PricingRulesListNameErrorComponent
        | ApiV1PricingRulesListProductKindErrorComponent
        | ApiV1PricingRulesListScopeErrorComponent
        | ApiV1PricingRulesListStateErrorComponent
        | ApiV1PricingRulesListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_rules_list_created_at_error_component import (
            ApiV1PricingRulesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_created_by_component_error_component import (
            ApiV1PricingRulesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_kind_error_component import (
            ApiV1PricingRulesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_name_error_component import (
            ApiV1PricingRulesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_scope_error_component import (
            ApiV1PricingRulesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_state_error_component import (
            ApiV1PricingRulesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_updated_at_error_component import (
            ApiV1PricingRulesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingRulesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesListCreatedByComponentErrorComponent):
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
        from ..models.api_v1_pricing_rules_list_created_at_error_component import (
            ApiV1PricingRulesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_created_by_component_error_component import (
            ApiV1PricingRulesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_kind_error_component import (
            ApiV1PricingRulesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_name_error_component import (
            ApiV1PricingRulesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_product_kind_error_component import (
            ApiV1PricingRulesListProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_scope_error_component import (
            ApiV1PricingRulesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_state_error_component import (
            ApiV1PricingRulesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_list_updated_at_error_component import (
            ApiV1PricingRulesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingRulesListCreatedAtErrorComponent
                | ApiV1PricingRulesListCreatedByComponentErrorComponent
                | ApiV1PricingRulesListKindErrorComponent
                | ApiV1PricingRulesListNameErrorComponent
                | ApiV1PricingRulesListProductKindErrorComponent
                | ApiV1PricingRulesListScopeErrorComponent
                | ApiV1PricingRulesListStateErrorComponent
                | ApiV1PricingRulesListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_0 = (
                        ApiV1PricingRulesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_1 = (
                        ApiV1PricingRulesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_2 = (
                        ApiV1PricingRulesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_3 = (
                        ApiV1PricingRulesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_4 = (
                        ApiV1PricingRulesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_5 = (
                        ApiV1PricingRulesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_list_error_type_6 = (
                        ApiV1PricingRulesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_rules_list_error_type_7 = (
                    ApiV1PricingRulesListProductKindErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_rules_list_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_rules_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_rules_list_validation_error.additional_properties = d
        return api_v1_pricing_rules_list_validation_error

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
