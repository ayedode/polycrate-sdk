from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_workspaces_list_created_at_error_component import (
        ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_created_by_component_error_component import (
        ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_kind_error_component import (
        ApiV1PricingQuoteWorkspacesListKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_name_error_component import (
        ApiV1PricingQuoteWorkspacesListNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_quote_error_component import (
        ApiV1PricingQuoteWorkspacesListQuoteErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_scope_error_component import (
        ApiV1PricingQuoteWorkspacesListScopeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_state_error_component import (
        ApiV1PricingQuoteWorkspacesListStateErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_list_updated_at_error_component import (
        ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteWorkspacesListValidationError")


@_attrs_define
class ApiV1PricingQuoteWorkspacesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent |
            ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent |
            ApiV1PricingQuoteWorkspacesListKindErrorComponent | ApiV1PricingQuoteWorkspacesListNameErrorComponent |
            ApiV1PricingQuoteWorkspacesListQuoteErrorComponent | ApiV1PricingQuoteWorkspacesListScopeErrorComponent |
            ApiV1PricingQuoteWorkspacesListStateErrorComponent | ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent
        | ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent
        | ApiV1PricingQuoteWorkspacesListKindErrorComponent
        | ApiV1PricingQuoteWorkspacesListNameErrorComponent
        | ApiV1PricingQuoteWorkspacesListQuoteErrorComponent
        | ApiV1PricingQuoteWorkspacesListScopeErrorComponent
        | ApiV1PricingQuoteWorkspacesListStateErrorComponent
        | ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_workspaces_list_created_at_error_component import (
            ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_created_by_component_error_component import (
            ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_kind_error_component import (
            ApiV1PricingQuoteWorkspacesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_name_error_component import (
            ApiV1PricingQuoteWorkspacesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_scope_error_component import (
            ApiV1PricingQuoteWorkspacesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_state_error_component import (
            ApiV1PricingQuoteWorkspacesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_updated_at_error_component import (
            ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent):
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
        from ..models.api_v1_pricing_quote_workspaces_list_created_at_error_component import (
            ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_created_by_component_error_component import (
            ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_kind_error_component import (
            ApiV1PricingQuoteWorkspacesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_name_error_component import (
            ApiV1PricingQuoteWorkspacesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_quote_error_component import (
            ApiV1PricingQuoteWorkspacesListQuoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_scope_error_component import (
            ApiV1PricingQuoteWorkspacesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_state_error_component import (
            ApiV1PricingQuoteWorkspacesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_list_updated_at_error_component import (
            ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent
                | ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent
                | ApiV1PricingQuoteWorkspacesListKindErrorComponent
                | ApiV1PricingQuoteWorkspacesListNameErrorComponent
                | ApiV1PricingQuoteWorkspacesListQuoteErrorComponent
                | ApiV1PricingQuoteWorkspacesListScopeErrorComponent
                | ApiV1PricingQuoteWorkspacesListStateErrorComponent
                | ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_0 = (
                        ApiV1PricingQuoteWorkspacesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_1 = (
                        ApiV1PricingQuoteWorkspacesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_2 = (
                        ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_3 = (
                        ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_4 = (
                        ApiV1PricingQuoteWorkspacesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_5 = (
                        ApiV1PricingQuoteWorkspacesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_6 = (
                        ApiV1PricingQuoteWorkspacesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_7 = (
                    ApiV1PricingQuoteWorkspacesListQuoteErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_workspaces_list_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_workspaces_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_workspaces_list_validation_error.additional_properties = d
        return api_v1_pricing_quote_workspaces_list_validation_error

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
