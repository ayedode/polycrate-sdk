from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_sinks_list_created_at_error_component import (
        ApiV1NotificationsSinksListCreatedAtErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_list_created_by_component_error_component import (
        ApiV1NotificationsSinksListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_list_kind_error_component import (
        ApiV1NotificationsSinksListKindErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_list_name_error_component import (
        ApiV1NotificationsSinksListNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_list_scope_error_component import (
        ApiV1NotificationsSinksListScopeErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_list_state_error_component import (
        ApiV1NotificationsSinksListStateErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_list_updated_at_error_component import (
        ApiV1NotificationsSinksListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsSinksListValidationError")


@_attrs_define
class ApiV1NotificationsSinksListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsSinksListCreatedAtErrorComponent |
            ApiV1NotificationsSinksListCreatedByComponentErrorComponent | ApiV1NotificationsSinksListKindErrorComponent |
            ApiV1NotificationsSinksListNameErrorComponent | ApiV1NotificationsSinksListScopeErrorComponent |
            ApiV1NotificationsSinksListStateErrorComponent | ApiV1NotificationsSinksListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsSinksListCreatedAtErrorComponent
        | ApiV1NotificationsSinksListCreatedByComponentErrorComponent
        | ApiV1NotificationsSinksListKindErrorComponent
        | ApiV1NotificationsSinksListNameErrorComponent
        | ApiV1NotificationsSinksListScopeErrorComponent
        | ApiV1NotificationsSinksListStateErrorComponent
        | ApiV1NotificationsSinksListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_sinks_list_created_at_error_component import (
            ApiV1NotificationsSinksListCreatedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_kind_error_component import (
            ApiV1NotificationsSinksListKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_name_error_component import (
            ApiV1NotificationsSinksListNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_scope_error_component import (
            ApiV1NotificationsSinksListScopeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_state_error_component import (
            ApiV1NotificationsSinksListStateErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_updated_at_error_component import (
            ApiV1NotificationsSinksListUpdatedAtErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsSinksListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksListScopeErrorComponent):
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
        from ..models.api_v1_notifications_sinks_list_created_at_error_component import (
            ApiV1NotificationsSinksListCreatedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_created_by_component_error_component import (
            ApiV1NotificationsSinksListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_kind_error_component import (
            ApiV1NotificationsSinksListKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_name_error_component import (
            ApiV1NotificationsSinksListNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_scope_error_component import (
            ApiV1NotificationsSinksListScopeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_state_error_component import (
            ApiV1NotificationsSinksListStateErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_list_updated_at_error_component import (
            ApiV1NotificationsSinksListUpdatedAtErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsSinksListCreatedAtErrorComponent
                | ApiV1NotificationsSinksListCreatedByComponentErrorComponent
                | ApiV1NotificationsSinksListKindErrorComponent
                | ApiV1NotificationsSinksListNameErrorComponent
                | ApiV1NotificationsSinksListScopeErrorComponent
                | ApiV1NotificationsSinksListStateErrorComponent
                | ApiV1NotificationsSinksListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_list_error_type_0 = (
                        ApiV1NotificationsSinksListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_list_error_type_1 = (
                        ApiV1NotificationsSinksListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_list_error_type_2 = (
                        ApiV1NotificationsSinksListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_list_error_type_3 = (
                        ApiV1NotificationsSinksListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_list_error_type_4 = (
                        ApiV1NotificationsSinksListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_list_error_type_5 = (
                        ApiV1NotificationsSinksListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_sinks_list_error_type_6 = (
                    ApiV1NotificationsSinksListCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_sinks_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_sinks_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_sinks_list_validation_error.additional_properties = d
        return api_v1_notifications_sinks_list_validation_error

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
