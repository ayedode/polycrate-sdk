from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quotes_list_created_at_error_component import (
        ApiV1PricingQuotesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_list_created_by_component_error_component import (
        ApiV1PricingQuotesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_list_kind_error_component import ApiV1PricingQuotesListKindErrorComponent
    from ..models.api_v1_pricing_quotes_list_name_error_component import ApiV1PricingQuotesListNameErrorComponent
    from ..models.api_v1_pricing_quotes_list_scope_error_component import ApiV1PricingQuotesListScopeErrorComponent
    from ..models.api_v1_pricing_quotes_list_state_error_component import ApiV1PricingQuotesListStateErrorComponent
    from ..models.api_v1_pricing_quotes_list_updated_at_error_component import (
        ApiV1PricingQuotesListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuotesListValidationError")


@_attrs_define
class ApiV1PricingQuotesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuotesListCreatedAtErrorComponent |
            ApiV1PricingQuotesListCreatedByComponentErrorComponent | ApiV1PricingQuotesListKindErrorComponent |
            ApiV1PricingQuotesListNameErrorComponent | ApiV1PricingQuotesListScopeErrorComponent |
            ApiV1PricingQuotesListStateErrorComponent | ApiV1PricingQuotesListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuotesListCreatedAtErrorComponent
        | ApiV1PricingQuotesListCreatedByComponentErrorComponent
        | ApiV1PricingQuotesListKindErrorComponent
        | ApiV1PricingQuotesListNameErrorComponent
        | ApiV1PricingQuotesListScopeErrorComponent
        | ApiV1PricingQuotesListStateErrorComponent
        | ApiV1PricingQuotesListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quotes_list_created_at_error_component import (
            ApiV1PricingQuotesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_kind_error_component import (
            ApiV1PricingQuotesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_name_error_component import (
            ApiV1PricingQuotesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_scope_error_component import (
            ApiV1PricingQuotesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_state_error_component import (
            ApiV1PricingQuotesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_updated_at_error_component import (
            ApiV1PricingQuotesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuotesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesListScopeErrorComponent):
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
        from ..models.api_v1_pricing_quotes_list_created_at_error_component import (
            ApiV1PricingQuotesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_created_by_component_error_component import (
            ApiV1PricingQuotesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_kind_error_component import (
            ApiV1PricingQuotesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_name_error_component import (
            ApiV1PricingQuotesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_scope_error_component import (
            ApiV1PricingQuotesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_state_error_component import (
            ApiV1PricingQuotesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_list_updated_at_error_component import (
            ApiV1PricingQuotesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuotesListCreatedAtErrorComponent
                | ApiV1PricingQuotesListCreatedByComponentErrorComponent
                | ApiV1PricingQuotesListKindErrorComponent
                | ApiV1PricingQuotesListNameErrorComponent
                | ApiV1PricingQuotesListScopeErrorComponent
                | ApiV1PricingQuotesListStateErrorComponent
                | ApiV1PricingQuotesListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_list_error_type_0 = (
                        ApiV1PricingQuotesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_list_error_type_1 = (
                        ApiV1PricingQuotesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_list_error_type_2 = (
                        ApiV1PricingQuotesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_list_error_type_3 = (
                        ApiV1PricingQuotesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_list_error_type_4 = (
                        ApiV1PricingQuotesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_list_error_type_5 = (
                        ApiV1PricingQuotesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quotes_list_error_type_6 = (
                    ApiV1PricingQuotesListCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quotes_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quotes_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quotes_list_validation_error.additional_properties = d
        return api_v1_pricing_quotes_list_validation_error

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
