from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_notifications_list_created_at_error_component import (
        ApiV1NotificationsNotificationsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_notifications_notifications_list_created_by_component_error_component import (
        ApiV1NotificationsNotificationsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_notifications_notifications_list_kind_error_component import (
        ApiV1NotificationsNotificationsListKindErrorComponent,
    )
    from ..models.api_v1_notifications_notifications_list_name_error_component import (
        ApiV1NotificationsNotificationsListNameErrorComponent,
    )
    from ..models.api_v1_notifications_notifications_list_scope_error_component import (
        ApiV1NotificationsNotificationsListScopeErrorComponent,
    )
    from ..models.api_v1_notifications_notifications_list_state_error_component import (
        ApiV1NotificationsNotificationsListStateErrorComponent,
    )
    from ..models.api_v1_notifications_notifications_list_updated_at_error_component import (
        ApiV1NotificationsNotificationsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsNotificationsListValidationError")


@_attrs_define
class ApiV1NotificationsNotificationsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsNotificationsListCreatedAtErrorComponent |
            ApiV1NotificationsNotificationsListCreatedByComponentErrorComponent |
            ApiV1NotificationsNotificationsListKindErrorComponent | ApiV1NotificationsNotificationsListNameErrorComponent |
            ApiV1NotificationsNotificationsListScopeErrorComponent | ApiV1NotificationsNotificationsListStateErrorComponent
            | ApiV1NotificationsNotificationsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsNotificationsListCreatedAtErrorComponent
        | ApiV1NotificationsNotificationsListCreatedByComponentErrorComponent
        | ApiV1NotificationsNotificationsListKindErrorComponent
        | ApiV1NotificationsNotificationsListNameErrorComponent
        | ApiV1NotificationsNotificationsListScopeErrorComponent
        | ApiV1NotificationsNotificationsListStateErrorComponent
        | ApiV1NotificationsNotificationsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_notifications_list_created_at_error_component import (
            ApiV1NotificationsNotificationsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_kind_error_component import (
            ApiV1NotificationsNotificationsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_name_error_component import (
            ApiV1NotificationsNotificationsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_scope_error_component import (
            ApiV1NotificationsNotificationsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_state_error_component import (
            ApiV1NotificationsNotificationsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_updated_at_error_component import (
            ApiV1NotificationsNotificationsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsNotificationsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsNotificationsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsNotificationsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsNotificationsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsNotificationsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsNotificationsListScopeErrorComponent):
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
        from ..models.api_v1_notifications_notifications_list_created_at_error_component import (
            ApiV1NotificationsNotificationsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_created_by_component_error_component import (
            ApiV1NotificationsNotificationsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_kind_error_component import (
            ApiV1NotificationsNotificationsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_name_error_component import (
            ApiV1NotificationsNotificationsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_scope_error_component import (
            ApiV1NotificationsNotificationsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_state_error_component import (
            ApiV1NotificationsNotificationsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_notifications_list_updated_at_error_component import (
            ApiV1NotificationsNotificationsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsNotificationsListCreatedAtErrorComponent
                | ApiV1NotificationsNotificationsListCreatedByComponentErrorComponent
                | ApiV1NotificationsNotificationsListKindErrorComponent
                | ApiV1NotificationsNotificationsListNameErrorComponent
                | ApiV1NotificationsNotificationsListScopeErrorComponent
                | ApiV1NotificationsNotificationsListStateErrorComponent
                | ApiV1NotificationsNotificationsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_notifications_list_error_type_0 = (
                        ApiV1NotificationsNotificationsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_notifications_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_notifications_list_error_type_1 = (
                        ApiV1NotificationsNotificationsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_notifications_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_notifications_list_error_type_2 = (
                        ApiV1NotificationsNotificationsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_notifications_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_notifications_list_error_type_3 = (
                        ApiV1NotificationsNotificationsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_notifications_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_notifications_list_error_type_4 = (
                        ApiV1NotificationsNotificationsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_notifications_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_notifications_list_error_type_5 = (
                        ApiV1NotificationsNotificationsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_notifications_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_notifications_list_error_type_6 = (
                    ApiV1NotificationsNotificationsListCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_notifications_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_notifications_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_notifications_list_validation_error.additional_properties = d
        return api_v1_notifications_notifications_list_validation_error

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
