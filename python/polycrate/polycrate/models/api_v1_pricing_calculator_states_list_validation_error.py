from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_calculator_states_list_created_at_error_component import (
        ApiV1PricingCalculatorStatesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_list_created_by_component_error_component import (
        ApiV1PricingCalculatorStatesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_list_kind_error_component import (
        ApiV1PricingCalculatorStatesListKindErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_list_name_error_component import (
        ApiV1PricingCalculatorStatesListNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_list_scope_error_component import (
        ApiV1PricingCalculatorStatesListScopeErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_list_state_error_component import (
        ApiV1PricingCalculatorStatesListStateErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_list_updated_at_error_component import (
        ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCalculatorStatesListValidationError")


@_attrs_define
class ApiV1PricingCalculatorStatesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCalculatorStatesListCreatedAtErrorComponent |
            ApiV1PricingCalculatorStatesListCreatedByComponentErrorComponent |
            ApiV1PricingCalculatorStatesListKindErrorComponent | ApiV1PricingCalculatorStatesListNameErrorComponent |
            ApiV1PricingCalculatorStatesListScopeErrorComponent | ApiV1PricingCalculatorStatesListStateErrorComponent |
            ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCalculatorStatesListCreatedAtErrorComponent
        | ApiV1PricingCalculatorStatesListCreatedByComponentErrorComponent
        | ApiV1PricingCalculatorStatesListKindErrorComponent
        | ApiV1PricingCalculatorStatesListNameErrorComponent
        | ApiV1PricingCalculatorStatesListScopeErrorComponent
        | ApiV1PricingCalculatorStatesListStateErrorComponent
        | ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_calculator_states_list_created_at_error_component import (
            ApiV1PricingCalculatorStatesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_kind_error_component import (
            ApiV1PricingCalculatorStatesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_name_error_component import (
            ApiV1PricingCalculatorStatesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_scope_error_component import (
            ApiV1PricingCalculatorStatesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_state_error_component import (
            ApiV1PricingCalculatorStatesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_updated_at_error_component import (
            ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCalculatorStatesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesListScopeErrorComponent):
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
        from ..models.api_v1_pricing_calculator_states_list_created_at_error_component import (
            ApiV1PricingCalculatorStatesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_created_by_component_error_component import (
            ApiV1PricingCalculatorStatesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_kind_error_component import (
            ApiV1PricingCalculatorStatesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_name_error_component import (
            ApiV1PricingCalculatorStatesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_scope_error_component import (
            ApiV1PricingCalculatorStatesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_state_error_component import (
            ApiV1PricingCalculatorStatesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_list_updated_at_error_component import (
            ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCalculatorStatesListCreatedAtErrorComponent
                | ApiV1PricingCalculatorStatesListCreatedByComponentErrorComponent
                | ApiV1PricingCalculatorStatesListKindErrorComponent
                | ApiV1PricingCalculatorStatesListNameErrorComponent
                | ApiV1PricingCalculatorStatesListScopeErrorComponent
                | ApiV1PricingCalculatorStatesListStateErrorComponent
                | ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_list_error_type_0 = (
                        ApiV1PricingCalculatorStatesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_list_error_type_1 = (
                        ApiV1PricingCalculatorStatesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_list_error_type_2 = (
                        ApiV1PricingCalculatorStatesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_list_error_type_3 = (
                        ApiV1PricingCalculatorStatesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_list_error_type_4 = (
                        ApiV1PricingCalculatorStatesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_list_error_type_5 = (
                        ApiV1PricingCalculatorStatesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_calculator_states_list_error_type_6 = (
                    ApiV1PricingCalculatorStatesListCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_calculator_states_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_calculator_states_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_calculator_states_list_validation_error.additional_properties = d
        return api_v1_pricing_calculator_states_list_validation_error

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
